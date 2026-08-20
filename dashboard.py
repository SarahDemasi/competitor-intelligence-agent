"""
Dashboard for Competitor Intelligence Agent
Displays competitor monitoring data via web interface
"""

from flask import Flask, render_template, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime
from config import DATABASE_FILE, DASHBOARD_PORT, DASHBOARD_HOST
from agent import CompetitorIntelligenceAgent

app = Flask(__name__)
CORS(app)

# Initialize agent
agent = CompetitorIntelligenceAgent()

@app.route('/')
def index():
    """Serve the dashboard"""
    return render_template('index.html')

@app.route('/api/summary')
def get_summary():
    """Get competitor intelligence summary"""
    summary = agent.get_summary()
    return jsonify(summary)

@app.route('/api/competitors')
def get_competitors():
    """Get list of all competitors and their status"""
    competitors_data = agent.data.get("competitors", {})
    return jsonify(competitors_data)

@app.route('/api/changes')
def get_changes():
    """Get recent changes detected"""
    changes = agent.data.get("changes", [])
    # Return last 50 changes
    return jsonify(changes[-50:])

@app.route('/api/monitor')
def trigger_monitor():
    """Trigger a manual monitoring run"""
    try:
        changes = agent.monitor_competitors()
        return jsonify({
            "status": "success",
            "changes_found": len(changes),
            "timestamp": datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/api/competitor/<competitor_name>')
def get_competitor_details(competitor_name):
    """Get detailed information about a specific competitor"""
    if competitor_name in agent.data.get("competitors", {}):
        competitor_data = agent.data["competitors"][competitor_name]
        return jsonify(competitor_data)
    return jsonify({"error": "Competitor not found"}), 404

@app.route('/api/fees')
def get_fees():
    """Get fee comparison data"""
    fees_data = agent.get_fee_comparison()
    return jsonify(fees_data)

@app.route('/api/performance')
def get_performance():
    """Get investment performance comparison data"""
    performance_data = agent.get_performance_comparison()
    return jsonify(performance_data)

@app.route('/api/education')
def get_education():
    """Get retirement education & guidance comparison data"""
    education_data = agent.get_retirement_education_comparison()
    return jsonify(education_data)

@app.route('/api/awards')
def get_awards():
    """Get super fund awards and rankings comparison data"""
    awards_data = agent.get_awards_comparison()
    return jsonify(awards_data)

@app.route('/api/media')
def get_media_investment():
    """Get competitor media investment spend by channel"""
    media_data = agent.get_media_investment_comparison()
    return jsonify(media_data)

@app.route('/api/award-ratings')
def get_award_ratings():
    """Get award ratings comparison across all competitors"""
    competitors_data = agent.data.get("competitors", {})
    award_ratings = {}

    for name, data in competitors_data.items():
        if data.get("award_ratings"):
            award_ratings[name] = data["award_ratings"]
        else:
            award_ratings[name] = {
                "competitor": name,
                "stars": None,
                "awards": [],
                "rating_keywords_found": []
            }

    return jsonify(award_ratings)

@app.route('/api/products-and-awards')
def get_products_and_awards():
    """Get products and their awards by competitor"""
    competitors_data = agent.data.get("competitors", {})
    products_awards = {}

    for name, data in competitors_data.items():
        if data.get("products_and_awards"):
            products_awards[name] = data["products_and_awards"]
        else:
            products_awards[name] = {}

    return jsonify(products_awards)

if __name__ == '__main__':
    print(f"Starting dashboard on http://{DASHBOARD_HOST}:{DASHBOARD_PORT}")
    app.run(host=DASHBOARD_HOST, port=DASHBOARD_PORT, debug=True)
