# Competitor Intelligence Agent 🎯

An AI-enabled agent that monitors super fund competitors and generates actionable intelligence summaries for marketing teams.

## What It Does

This agent automatically:
- ✅ Monitors competitor websites for changes
- 📊 Detects new announcements, campaigns, and product updates
- 🎯 Extracts relevant keywords (fees, promotions, ESG, performance, etc.)
- 📈 Maintains a searchable history of competitor activity
- 💡 Displays insights via an interactive dashboard

## Quick Start

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run a Monitoring Scan

```bash
python agent.py
```

This will scan all competitor websites and save findings to `competitor_data.json`.

### 3. Start the Dashboard

```bash
python dashboard.py
```

Then open your browser to: **http://localhost:5000**

## What You'll See in the Dashboard

- **Competitor Status**: Which competitors have been checked
- **Recent Changes**: Latest detected updates with keywords
- **Statistics**: Total competitors monitored and changes found
- **Manual Monitoring**: Button to run scans on demand

## File Structure

```
competitor-intelligence-agent/
├── agent.py                 # Core monitoring agent
├── dashboard.py             # Flask web dashboard
├── config.py               # Configuration & competitor list
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html         # Dashboard UI
├── competitor_data.json    # Stored findings (auto-generated)
└── README.md              # This file
```

## Competitors Being Tracked

- AMP
- Australian Retirement Trust
- AustralianSuper
- Aware Super
- Colonial First State
- Industry SuperFunds
- MLC
- REST Industry Super
- UniSuper
- HostPlus
- HESTA

## Configuration

Edit `config.py` to:
- Add/remove competitors
- Change keywords to track
- Adjust monitoring frequency
- Modify dashboard port

## Next Steps

### Coming Soon:
- 📧 Email alerts for significant changes
- 🔔 Slack notifications
- 📱 Mobile app
- 📈 Trend analysis
- 🌐 Multi-channel monitoring (social media, news)
- 📊 Competitive analysis reports

## Troubleshooting

**Dashboard won't load?**
- Make sure you ran `python dashboard.py`
- Check if port 5000 is available
- Try a different port in `config.py`

**No data showing up?**
- Run `python agent.py` first to generate data
- Check that `competitor_data.json` was created
- Verify competitor URLs are accessible

**Getting errors?**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check your internet connection
- Some websites may block automated requests

## Tips for Success

1. **Run monitoring regularly**: Set up a scheduled task or cron job
2. **Review the dashboard weekly**: Look for patterns and trends
3. **Adjust keywords**: Add industry-specific terms relevant to your business
4. **Share insights**: Export findings to share with your team

---

Built with ❤️ for smarter marketing decisions
