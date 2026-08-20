"""
Competitor Intelligence Agent
Monitors competitor websites and tracks changes
"""

import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime
from config import COMPETITORS, KEYWORDS, DATABASE_FILE, ADMIN_FEES, INVESTMENT_FEES, PENSION_ACCOUNT_FEES, PENSION_BONUSES, INVESTMENT_PERFORMANCE, RETIREMENT_EDUCATION, AWARDS_RANKINGS, MEDIA_INVESTMENT
import hashlib

class CompetitorIntelligenceAgent:
    """Main agent for monitoring competitor activity"""
    
    def __init__(self):
        self.data_file = DATABASE_FILE
        self.load_data()
    
    def load_data(self):
        """Load existing competitor data from file"""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {"competitors": {}, "changes": []}
    
    def save_data(self):
        """Save competitor data to file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def fetch_competitor_content(self, competitor_name, url):
        """
        Fetch content from competitor website
        Returns: page text content
        """
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            
            # Get text
            text = soup.get_text()
            # Clean up whitespace
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = ' '.join(chunk for chunk in chunks if chunk)
            
            return text
        except Exception as e:
            print(f"Error fetching {competitor_name} ({url}): {str(e)}")
            return None
    
    def detect_changes(self, competitor_name, new_content):
        """
        Detect changes in competitor content
        Returns: list of detected changes
        """
        changes = []
        
        if competitor_name not in self.data["competitors"]:
            self.data["competitors"][competitor_name] = {
                "url": COMPETITORS[competitor_name],
                "last_checked": None,
                "content_hash": None,
                "last_content": None
            }
        
        competitor_data = self.data["competitors"][competitor_name]
        new_hash = hashlib.md5(new_content.encode()).hexdigest()
        
        # Check if content has changed
        if competitor_data["content_hash"] and competitor_data["content_hash"] != new_hash:
            changes.append({
                "type": "content_update",
                "competitor": competitor_name,
                "timestamp": datetime.now().isoformat(),
                "keywords_found": self.extract_keywords(new_content)
            })
        
        # Update competitor data
        competitor_data["content_hash"] = new_hash
        competitor_data["last_checked"] = datetime.now().isoformat()
        competitor_data["last_content"] = new_content[:5000]  # Store first 5000 chars
        
        return changes
    
    def extract_keywords(self, content):
        """Extract relevant keywords from content"""
        content_lower = content.lower()
        found_keywords = []
        
        for keyword in KEYWORDS:
            if keyword.lower() in content_lower:
                found_keywords.append(keyword)
        
        return found_keywords
    
    def monitor_competitors(self):
        """
        Main monitoring function
        Fetches content from all competitors and detects changes
        """
        print(f"\n{'='*60}")
        print(f"Starting competitor monitoring at {datetime.now().isoformat()}")
        print(f"{'='*60}")
        
        all_changes = []
        
        for competitor_name, url in COMPETITORS.items():
            print(f"\nMonitoring {competitor_name}...")
            content = self.fetch_competitor_content(competitor_name, url)
            
            if content:
                changes = self.detect_changes(competitor_name, content)
                all_changes.extend(changes)
                print(f"✓ {competitor_name} checked successfully")
                if changes:
                    print(f"  Found {len(changes)} change(s)")
            else:
                print(f"✗ Failed to fetch {competitor_name}")
        
        # Save updated data
        self.data["changes"].extend(all_changes)
        self.save_data()
        
        print(f"\n{'='*60}")
        print(f"Monitoring complete. Found {len(all_changes)} total changes.")
        print(f"{'='*60}\n")
        
        return all_changes
    
    def get_summary(self):
        """Generate a summary of competitor intelligence"""
        summary = {
            "total_competitors": len(self.data["competitors"]),
            "competitors": self.data["competitors"],
            "recent_changes": self.data["changes"][-10:] if self.data["changes"] else [],
            "last_updated": datetime.now().isoformat()
        }
        return summary
    
    def get_fee_comparison(self):
        """Get fee comparison data for all competitors"""
        admin_fees_data = []
        investment_fees_data = []
        pension_fees_data = []
        pension_bonus_data = []
        
        for competitor_name in ADMIN_FEES.keys():
            admin_fees_data.append({
                "name": competitor_name,
                "fee": ADMIN_FEES[competitor_name],
                "url": COMPETITORS.get(competitor_name, "N/A")
            })
            investment_fees_data.append({
                "name": competitor_name,
                "fee": INVESTMENT_FEES[competitor_name],
                "url": COMPETITORS.get(competitor_name, "N/A")
            })
            pension_fees_data.append({
                "name": competitor_name,
                "fee": PENSION_ACCOUNT_FEES[competitor_name],
                "url": COMPETITORS.get(competitor_name, "N/A")
            })
            pension_bonus_data.append({
                "name": competitor_name,
                "bonus": PENSION_BONUSES[competitor_name],
                "url": COMPETITORS.get(competitor_name, "N/A")
            })
        
        # Sort by fee (lowest first) for fees
        admin_fees_data.sort(key=lambda x: x["fee"])
        investment_fees_data.sort(key=lambda x: x["fee"])
        pension_fees_data.sort(key=lambda x: x["fee"])
        # Sort by bonus (highest first) for bonuses
        pension_bonus_data.sort(key=lambda x: x["bonus"], reverse=True)
        
        return {
            "admin": admin_fees_data,
            "investment": investment_fees_data,
            "pension": pension_fees_data,
            "bonus": pension_bonus_data
        }
    
    def get_performance_comparison(self):
        """Get investment performance comparison data for all competitors"""
        balanced_data = []
        growth_data = []
        high_growth_data = []
        conservative_data = []
        
        for competitor_name, performance in INVESTMENT_PERFORMANCE.items():
            balanced_data.append({
                "name": competitor_name,
                "return": performance["balanced"],
                "url": COMPETITORS.get(competitor_name, "N/A")
            })
            growth_data.append({
                "name": competitor_name,
                "return": performance["growth"],
                "url": COMPETITORS.get(competitor_name, "N/A")
            })
            high_growth_data.append({
                "name": competitor_name,
                "return": performance["high_growth"],
                "url": COMPETITORS.get(competitor_name, "N/A")
            })
            conservative_data.append({
                "name": competitor_name,
                "return": performance["conservative"],
                "url": COMPETITORS.get(competitor_name, "N/A")
            })
        
        # Sort by return (highest first)
        balanced_data.sort(key=lambda x: x["return"], reverse=True)
        growth_data.sort(key=lambda x: x["return"], reverse=True)
        high_growth_data.sort(key=lambda x: x["return"], reverse=True)
        conservative_data.sort(key=lambda x: x["return"], reverse=True)
        
        return {
            "balanced": balanced_data,
            "growth": growth_data,
            "high_growth": high_growth_data,
            "conservative": conservative_data
        }
    
    def get_retirement_education_comparison(self):
        """Get retirement education & guidance comparison data for all competitors"""
        education_data = []
        
        for competitor_name, education in RETIREMENT_EDUCATION.items():
            # Calculate overall score
            overall_score = sum(education.values()) / len(education)
            education_data.append({
                "name": competitor_name,
                "hub_content": education["hub_content"],
                "readiness_tools": education["readiness_tools"],
                "planning_journeys": education["planning_journeys"],
                "seminars": education["seminars"],
                "age_communications": education["age_communications"],
                "age_pension_education": education["age_pension_education"],
                "overall_score": round(overall_score, 1),
                "url": COMPETITORS.get(competitor_name, "N/A")
            })
        
        # Sort by overall score (highest first)
        education_data.sort(key=lambda x: x["overall_score"], reverse=True)
        
        return education_data

    def get_awards_comparison(self):
        """Get super fund awards and rankings comparison data for all competitors"""
        awards_data = []

        for competitor_name, award_scores in AWARDS_RANKINGS.items():
            overall_score = sum(award_scores.values()) / len(award_scores)
            awards_data.append({
                "name": competitor_name,
                "chant_west": award_scores["chant_west"],
                "canstar": award_scores["canstar"],
                "superratings": award_scores["superratings"],
                "morningstar": award_scores["morningstar"],
                "money_magazine": award_scores["money_magazine"],
                "overall_score": round(overall_score, 1),
                "url": COMPETITORS.get(competitor_name, "N/A")
            })

        awards_data.sort(key=lambda x: x["overall_score"], reverse=True)
        return awards_data

    def get_media_investment_comparison(self):
        """Get competitor media investment by channel"""
        media_data = []

        for competitor_name, channels in MEDIA_INVESTMENT.items():
            total_spend = sum(channels.values())
            media_data.append({
                "name": competitor_name,
                "digital": channels["digital"],
                "social": channels["social"],
                "search": channels["search"],
                "tv": channels["tv"],
                "radio": channels["radio"],
                "outdoor": channels["outdoor"],
                "content": channels["content"],
                "sponsorship": channels["sponsorship"],
                "total_spend": round(total_spend, 1),
                "url": COMPETITORS.get(competitor_name, "N/A")
            })

        media_data.sort(key=lambda x: x["total_spend"], reverse=True)
        return media_data

if __name__ == "__main__":
    agent = CompetitorIntelligenceAgent()
    agent.monitor_competitors()
    summary = agent.get_summary()
    print("\nSummary:")
    print(json.dumps(summary, indent=2))
