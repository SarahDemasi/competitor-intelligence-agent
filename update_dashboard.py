# This script adds a new section to the dashboard for products and awards

html_file = 'templates/index.html'

# Read the file
with open(html_file, 'r') as f:
    content = f.read()

# Find where to insert the new section (before the existing ratings grid)
insert_marker = '<div class="panel" style="margin-bottom: 30px;">\n            <h2>🏆 Award Ratings Comparison</h2>'

new_section = '''<div class="panel" style="margin-bottom: 30px;">
            <h2>🏆 Awards by Brand & Product</h2>
            <div id="products-awards-container" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 20px;">
                <div class="loading">Loading awards data...</div>
            </div>
        </div>

        <div class="panel" style="margin-bottom: 30px;">
            <h2>🏆 Award Ratings Comparison</h2>'''

if insert_marker in content:
    content = content.replace(insert_marker, new_section)
    print("✓ Added products and awards section to dashboard")
else:
    print("✗ Could not find insertion point")

# Add CSS for product awards
css_insertion = '.no-data {\n            color: #999;\n            font-style: italic;\n        }'

new_css = '''.no-data {
            color: #999;
            font-style: italic;
        }
        
        .product-card {
            background: #f0f4ff;
            border: 1px solid #667eea;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 15px;
        }
        
        .product-name {
            font-weight: bold;
            color: #667eea;
            font-size: 16px;
            margin-bottom: 10px;
            padding-bottom: 8px;
            border-bottom: 2px solid #667eea;
        }
        
        .brand-name {
            color: #333;
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 15px;
            padding: 10px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 4px;
        }
        
        .award-list {
            list-style: none;
            margin: 0;
            padding: 0;
        }
        
        .award-list-item {
            padding: 6px 0;
            border-bottom: 1px solid #e0e0e0;
            font-size: 14px;
        }
        
        .award-list-item:last-child {
            border-bottom: none;
        }
        
        .award-list-item::before {
            content: "✓ ";
            color: #28a745;
            font-weight: bold;
            margin-right: 8px;
        }'''

if css_insertion in content:
    content = content.replace(css_insertion, new_css)
    print("✓ Added CSS styling for product awards")

# Write back
with open(html_file, 'w') as f:
    f.write(content)

print("Dashboard HTML updated successfully")
