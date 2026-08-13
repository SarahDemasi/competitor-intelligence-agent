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

if __name__ == "__main__":
    agent = CompetitorIntelligenceAgent()
    agent.monitor_competitors()
    summary = agent.get_summary()
    print("\nSummary:")
    print(json.dumps(summary, indent=2))
