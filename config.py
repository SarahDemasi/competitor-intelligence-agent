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

# Admin fees (annual percentage rates)
ADMIN_FEES = {
    "AMP": 0.35,
    "Australian Retirement Trust": 0.28,
    "AustralianSuper": 0.24,
    "Aware Super": 0.34,
    "Colonial First State": 0.45,
    "Industry SuperFunds": 0.30,
    "MLC": 0.55,
    "REST Industry Super": 0.32,
    "UniSuper": 0.20,
    "HostPlus": 0.31,
    "HESTA": 0.28
}

# Investment fees (annual percentage rates)
INVESTMENT_FEES = {
    "AMP": 0.40,
    "Australian Retirement Trust": 0.40,
    "AustralianSuper": 0.40,
    "Aware Super": 0.40,
    "Colonial First State": 0.40,
    "Industry SuperFunds": 0.40,
    "MLC": 0.50,
    "REST Industry Super": 0.40,
    "UniSuper": 0.40,
    "HostPlus": 0.40,
    "HESTA": 0.40
}

# Pension account fees (annual percentage rates)
PENSION_ACCOUNT_FEES = {
    "AMP": 0.42,
    "Australian Retirement Trust": 0.35,
    "AustralianSuper": 0.38,
    "Aware Super": 0.40,
    "Colonial First State": 0.48,
    "Industry SuperFunds": 0.38,
    "MLC": 0.60,
    "REST Industry Super": 0.38,
    "UniSuper": 0.35,
    "HostPlus": 0.40,
    "HESTA": 0.35
}

# Pension bonuses (annual percentage - employer/government co-contributions)
PENSION_BONUSES = {
    "AMP": 0.8,
    "Australian Retirement Trust": 0.9,
    "AustralianSuper": 0.85,
    "Aware Super": 0.87,
    "Colonial First State": 0.72,
    "Industry SuperFunds": 0.95,
    "MLC": 1.5,
    "REST Industry Super": 0.90,
    "UniSuper": 0.91,
    "HostPlus": 0.83,
    "HESTA": 0.93
}

# Investment performance claims (5-year average annual returns %)
INVESTMENT_PERFORMANCE = {
    "AMP": {
        "balanced": 6.8,
        "growth": 8.2,
        "high_growth": 9.5,
        "conservative": 4.5
    },
    "Australian Retirement Trust": {
        "balanced": 7.2,
        "growth": 8.9,
        "high_growth": 10.2,
        "conservative": 4.8
    },
    "AustralianSuper": {
        "balanced": 7.5,
        "growth": 9.1,
        "high_growth": 10.5,
        "conservative": 5.0
    },
    "Aware Super": {
        "balanced": 7.0,
        "growth": 8.6,
        "high_growth": 9.8,
        "conservative": 4.6
    },
    "Colonial First State": {
        "balanced": 6.9,
        "growth": 8.4,
        "high_growth": 9.6,
        "conservative": 4.4
    },
    "Industry SuperFunds": {
        "balanced": 7.3,
        "growth": 8.95,
        "high_growth": 10.3,
        "conservative": 4.9
    },
    "MLC": {
        "balanced": 6.5,
        "growth": 7.9,
        "high_growth": 9.1,
        "conservative": 4.2
    },
    "REST Industry Super": {
        "balanced": 7.1,
        "growth": 8.7,
        "high_growth": 10.0,
        "conservative": 4.7
    },
    "UniSuper": {
        "balanced": 7.4,
        "growth": 9.0,
        "high_growth": 10.4,
        "conservative": 4.9
    },
    "HostPlus": {
        "balanced": 6.9,
        "growth": 8.5,
        "high_growth": 9.7,
        "conservative": 4.5
    },
    "HESTA": {
        "balanced": 7.2,
        "growth": 8.8,
        "high_growth": 10.1,
        "conservative": 4.8
    }
}

# Retirement Education & Guidance Offerings (1-10 scale)
RETIREMENT_EDUCATION = {
    "AMP": {
        "hub_content": 7,
        "readiness_tools": 6,
        "planning_journeys": 6,
        "seminars": 5,
        "age_communications": 7,
        "age_pension_education": 6
    },
    "Australian Retirement Trust": {
        "hub_content": 8,
        "readiness_tools": 8,
        "planning_journeys": 7,
        "seminars": 7,
        "age_communications": 8,
        "age_pension_education": 8
    },
    "AustralianSuper": {
        "hub_content": 9,
        "readiness_tools": 9,
        "planning_journeys": 8,
        "seminars": 8,
        "age_communications": 9,
        "age_pension_education": 9
    },
    "Aware Super": {
        "hub_content": 7,
        "readiness_tools": 7,
        "planning_journeys": 6,
        "seminars": 6,
        "age_communications": 7,
        "age_pension_education": 7
    },
    "Colonial First State": {
        "hub_content": 6,
        "readiness_tools": 6,
        "planning_journeys": 5,
        "seminars": 5,
        "age_communications": 6,
        "age_pension_education": 5
    },
    "MLC": {
        "hub_content": 6,
        "readiness_tools": 7,
        "planning_journeys": 7,
        "seminars": 5,
        "age_communications": 6,
        "age_pension_education": 7
    },
    "REST Industry Super": {
        "hub_content": 7,
        "readiness_tools": 7,
        "planning_journeys": 7,
        "seminars": 7,
        "age_communications": 7,
        "age_pension_education": 7
    },
    "UniSuper": {
        "hub_content": 8,
        "readiness_tools": 8,
        "planning_journeys": 8,
        "seminars": 8,
        "age_communications": 8,
        "age_pension_education": 8
    },
    "HostPlus": {
        "hub_content": 7,
        "readiness_tools": 6,
        "planning_journeys": 6,
        "seminars": 6,
        "age_communications": 7,
        "age_pension_education": 6
    },
    "HESTA": {
        "hub_content": 8,
        "readiness_tools": 8,
        "planning_journeys": 7,
        "seminars": 8,
        "age_communications": 8,
        "age_pension_education": 8
    }
}

# Super fund awards and ratings comparison (1-10 score)
AWARDS_RANKINGS = {
    "AMP": {
        "chant_west": 6,
        "canstar": 6,
        "superratings": 6,
        "morningstar": 5,
        "money_magazine": 5
    },
    "Australian Retirement Trust": {
        "chant_west": 8,
        "canstar": 8,
        "superratings": 8,
        "morningstar": 7,
        "money_magazine": 7
    },
    "AustralianSuper": {
        "chant_west": 9,
        "canstar": 9,
        "superratings": 9,
        "morningstar": 8,
        "money_magazine": 8
    },
    "Aware Super": {
        "chant_west": 7,
        "canstar": 7,
        "superratings": 6,
        "morningstar": 6,
        "money_magazine": 6
    },
    "Colonial First State": {
        "chant_west": 5,
        "canstar": 5,
        "superratings": 5,
        "morningstar": 5,
        "money_magazine": 4
    },
    "MLC": {
        "chant_west": 5,
        "canstar": 5,
        "superratings": 6,
        "morningstar": 5,
        "money_magazine": 5
    },
    "REST Industry Super": {
        "chant_west": 6,
        "canstar": 6,
        "superratings": 6,
        "morningstar": 6,
        "money_magazine": 5
    },
    "UniSuper": {
        "chant_west": 8,
        "canstar": 8,
        "superratings": 8,
        "morningstar": 8,
        "money_magazine": 7
    },
    "HostPlus": {
        "chant_west": 7,
        "canstar": 7,
        "superratings": 7,
        "morningstar": 6,
        "money_magazine": 6
    },
    "HESTA": {
        "chant_west": 8,
        "canstar": 7,
        "superratings": 8,
        "morningstar": 7,
        "money_magazine": 7
    }
}

# Media investment by competitor by channel (AUD)
# Values reflect spend in AUD millions, period: 1 July 2025 to 30 June 2026.
MEDIA_INVESTMENT = {
    "AMP": {
        "digital": 8.5,
        "social": 5.3,
        "search": 4.2,
        "tv": 3.1,
        "radio": 1.6,
        "outdoor": 1.1,
        "content": 2.4,
        "sponsorship": 1.8
    },
    "Australian Retirement Trust": {
        "digital": 13.2,
        "social": 7.8,
        "search": 6.1,
        "tv": 5.5,
        "radio": 2.2,
        "outdoor": 2.1,
        "content": 3.8,
        "sponsorship": 3.2
    },
    "AustralianSuper": {
        "digital": 18.4,
        "social": 10.9,
        "search": 8.6,
        "tv": 7.6,
        "radio": 2.9,
        "outdoor": 2.8,
        "content": 5.1,
        "sponsorship": 4.3
    },
    "Aware Super": {
        "digital": 9.2,
        "social": 6.1,
        "search": 4.7,
        "tv": 2.8,
        "radio": 1.3,
        "outdoor": 1.4,
        "content": 2.6,
        "sponsorship": 1.9
    },
    "Colonial First State": {
        "digital": 7.4,
        "social": 4.7,
        "search": 3.8,
        "tv": 2.6,
        "radio": 1.2,
        "outdoor": 1.1,
        "content": 2.2,
        "sponsorship": 1.6
    },
    "MLC": {
        "digital": 3.9,
        "social": 2.4,
        "search": 2.0,
        "tv": 1.7,
        "radio": 0.9,
        "outdoor": 0.7,
        "content": 1.3,
        "sponsorship": 1.0
    },
    "REST Industry Super": {
        "digital": 10.1,
        "social": 6.4,
        "search": 4.9,
        "tv": 3.7,
        "radio": 1.7,
        "outdoor": 1.5,
        "content": 3.1,
        "sponsorship": 2.2
    },
    "UniSuper": {
        "digital": 12.7,
        "social": 7.5,
        "search": 6.2,
        "tv": 5.1,
        "radio": 2.1,
        "outdoor": 1.9,
        "content": 3.4,
        "sponsorship": 2.8
    },
    "HostPlus": {
        "digital": 10.8,
        "social": 6.9,
        "search": 5.2,
        "tv": 4.1,
        "radio": 1.8,
        "outdoor": 1.7,
        "content": 3.0,
        "sponsorship": 2.5
    },
    "HESTA": {
        "digital": 11.9,
        "social": 7.0,
        "search": 5.7,
        "tv": 4.9,
        "radio": 2.0,
        "outdoor": 1.8,
        "content": 3.2,
        "sponsorship": 2.9
    }
}
