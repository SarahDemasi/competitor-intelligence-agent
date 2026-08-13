"""
Configuration file for Competitor Intelligence Agent
"""

# Competitor list with their websites
COMPETITORS = {
    "AMP": "https://www.amp.com.au",
    "Australian Retirement Trust": "https://www.australianretirementtrust.com.au",
    "AustralianSuper": "https://www.australiansuper.com.au",
    "Aware Super": "https://www.awaresuperannuation.com.au",
    "Colonial First State": "https://www.cfs.com.au",
    "Industry SuperFunds": "https://www.industrysuperfunds.com.au",
    "MLC": "https://www.mlc.com.au",
    "REST Industry Super": "https://www.rest.com.au",
    "UniSuper": "https://www.unisuper.com.au",
    "HostPlus": "https://www.hostplus.com.au",
    "HESTA": "https://www.hesta.com.au"
}

# Keywords to track for intelligence gathering
KEYWORDS = [
    "fee",
    "price",
    "campaign",
    "promotion",
    "new product",
    "update",
    "announcement",
    "merger",
    "partnership",
    "sustainability",
    "ESG",
    "performance",
    "member",
    "benefit"
]

# Database settings
DATABASE_FILE = "competitor_data.json"

# Dashboard settings
DASHBOARD_PORT = 5000
DASHBOARD_HOST = "0.0.0.0"

# Monitoring schedule (in hours)
MONITORING_INTERVAL = 24
