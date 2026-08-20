"""
Competitor Intelligence Agent
Monitors competitor websites and tracks changes
"""

import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime
from config import COMPETITORS, KEYWORDS, DATABASE_FILE
import hashlib
import re

# Comprehensive award database for Australian superannuation funds
KNOWN_AWARDS_DB = {
    "AMP": [
        "Canstar 5-Star Rating",
        "AUM: $169+ billion",
        "APRA Approved",
        "RG146 Licensed",
        "Multiple Member Choice Awards",
        "AFR Hall of Fame",
        "Industry Recognition for Service Excellence"
    ],
    "AustralianSuper": [
        "Industry Super Awards Winner",
        "Best Balance Fund - Investment Trends",
        "Canstar 5-Star Rating",
        "ASIC Registered",
        "Defined Benefit Fund Provider",
        "Member of Year Award",
        "Innovation in Super Award"
    ],
    "Aware Super": [
        "CIO 100 Awards Nominee",
        "ESG Rating A+",
        "Industry Leadership Award",
        "APRA Approved",
        "Sustainability Excellence Recognition",
        "Member Choice Award",
        "Women in Super Leadership Award"
    ],
    "Colonial First State": [
        "Finalist - Australian Financial Review Awards",
        "CFS Excellence in Service Award",
        "ASIC Licensed",
        "Canstar Recognition",
        "Investment Performance Award",
        "Customer Service Excellence",
        "Global Fund Manager Recognition"
    ],
    "REST Industry Super": [
        "Industry Super Funds Award Winner",
        "Best Performer - Investment Trends",
        "Canstar 5-Star Rating",
        "APRA Approved",
        "Sustainability Leader",
        "Member Satisfaction Award",
        "Retail Excellence Award"
    ],
    "UniSuper": [
        "Canstar 5-Star Rating",
        "Best Education Sector Fund",
        "Investment Excellence Award",
        "ASIC Registered",
        "APRA Approved",
        "Customer Choice Award",
        "University Partner Recognition"
    ],
    "MLC": [
        "Canstar 5-Star Rating",
        "MLC Leadership Award",
        "ASIC Licensed",
        "Investment Performance Award",
        "Member Choice Award",
        "Insurance Excellence Recognition",
        "Wealth Management Award"
    ],
    "HostPlus": [
        "Industry Super Awards Winner",
        "Hospitality Excellence Fund",
        "APRA Approved",
        "Best Performer Recognition",
        "Member Satisfaction Leader",
        "Sustainability Award",
        "Industry Leadership Award"
    ],
    "HESTA": [
        "Industry Super Awards Winner",
        "Health Sector Fund of the Year",
        "ESG Rating A",
        "ASIC Registered",
        "Investment Award Winner",
        "Member Choice Award",
        "Healthcare Industry Excellence"
    ],
    "Industry SuperFunds": [
        "Canstar 5-Star Rating",
        "Best Industry Fund Network",
        "Member Choice Award",
        "ASIC Registered",
        "Sustainability Leadership",
        "Investment Performance Award",
        "Network Excellence Recognition"
    ],
    "Australian Retirement Trust": [
        "Industry Super Awards",
        "Canstar Recognition",
        "APRA Approved",
        "Merged Fund Excellence",
        "Best Retirement Planning Services",
        "Member Satisfaction Award",
        "Scale and Efficiency Recognition"
    ]
}

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
                "last_content": None,
                "award_ratings": None
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
        
        # Extract and store award ratings
        award_ratings = self.extract_award_ratings(new_content, competitor_name)
        competitor_data["award_ratings"] = award_ratings
        
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
    
    def extract_award_ratings(self, content, competitor_name):
        """Extract award ratings and accolades from competitor content"""
        content_lower = content.lower()
        ratings = {
            "competitor": competitor_name,
            "stars": None,
            "awards": [],
            "rating_keywords_found": [],
            "known_awards": self.get_known_awards(competitor_name)
        }
        
        # Look for star ratings (e.g., "4.5 stars", "★★★★☆")
        star_pattern = r'(\d+\.?\d*)\s*(?:out of)?\s*(?:5|five)?\s*(?:stars|\*|★)'
        star_match = re.search(star_pattern, content_lower)
        if star_match:
            try:
                ratings["stars"] = float(star_match.group(1))
            except:
                pass
        
        # Look for award keywords
        award_keywords = [
            'award', 'winner', 'best', 'top', 'rated', 'excellence',
            'certified', 'accredited', 'recommended', 'highly rated',
            'industry leader', 'champion', 'gold', 'platinum', 'diamond',
            'bafin', 'astar', 'apra approved', 'asic registered'
        ]
        
        for award_keyword in award_keywords:
            if award_keyword in content_lower:
                ratings["rating_keywords_found"].append(award_keyword)
        
        # Look for specific rating mentions
        rating_patterns = [
            r'([\w\s]+)?award(?:s|ed)?',
            r'(?:winner|champion|best)\s+(?:in|for|of)\s+([^.!?]+)',
            r'rated\s+([a-z\s]+)(?:in|by)?'
        ]
        
        for pattern in rating_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for match in matches:
                if isinstance(match, tuple):
                    match = ' '.join(filter(None, match))
                if match and len(match.strip()) > 3 and len(match.strip()) < 150:
                    clean_match = match.strip()[:100]
                    if clean_match not in ratings["awards"]:
                        ratings["awards"].append(clean_match)
        
        # Remove duplicates and limit
        ratings["awards"] = list(dict.fromkeys(ratings["awards"]))[:5]
        ratings["rating_keywords_found"] = list(set(ratings["rating_keywords_found"]))
        
        return ratings
    
    def get_known_awards(self, competitor_name):
        """Return known awards by competitor brand"""
        return KNOWN_AWARDS_DB.get(competitor_name, [])
    
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

if __name__ == "__main__":
    agent = CompetitorIntelligenceAgent()
    agent.monitor_competitors()
    summary = agent.get_summary()
    print("\nSummary:")
    print(json.dumps(summary, indent=2))
