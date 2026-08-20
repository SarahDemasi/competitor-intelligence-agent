html_file = 'templates/index.html'

with open(html_file, 'r') as f:
    lines = f.readlines()

# Find where loadAwardRatings is defined and add our new function before it
insert_index = -1
for i, line in enumerate(lines):
    if 'function loadAwardRatings()' in line:
        insert_index = i
        break

if insert_index > 0:
    new_function = '''        function loadProductsAndAwards() {
            fetch('/api/products-and-awards')
                .then(response => response.json())
                .then(data => {
                    const container = document.getElementById('products-awards-container');
                    container.innerHTML = '';
                    
                    if (Object.keys(data).length === 0) {
                        container.innerHTML = '<div class="loading">No award data available</div>';
                        return;
                    }
                    
                    // Create cards for each brand
                    Object.entries(data).forEach(([brand, products]) => {
                        const brandDiv = document.createElement('div');
                        brandDiv.className = 'panel';
                        brandDiv.style.margin = '0';
                        
                        let brandHTML = `<div class="brand-name">${brand}</div>`;
                        
                        // Display products and their awards
                        if (Object.keys(products).length === 0) {
                            brandHTML += '<div class="no-data">No award data available</div>';
                        } else {
                            Object.entries(products).forEach(([product, awards]) => {
                                brandHTML += `
                                    <div class="product-card">
                                        <div class="product-name">${product}</div>
                                        <ul class="award-list">
                                            ${awards.map(award => `<li class="award-list-item">${award}</li>`).join('')}
                                        </ul>
                                    </div>
                                `;
                            });
                        }
                        
                        brandDiv.innerHTML = brandHTML;
                        container.appendChild(brandDiv);
                    });
                })
                .catch(error => console.error('Error loading products and awards:', error));
        }
        
        '''
    lines.insert(insert_index, new_function)
    
    # Also update loadDashboard to call loadProductsAndAwards
    for i, line in enumerate(lines):
        if 'function loadDashboard()' in line:
            # Find the closing of loadDashboard and add the call
            for j in range(i, min(i + 20, len(lines))):
                if 'loadAwardRatings()' in lines[j]:
                    # Add before loadAwardRatings
                    lines[j] = '            loadProductsAndAwards();\n' + lines[j]
                    break
            break
    
    with open(html_file, 'w') as f:
        f.writelines(lines)
    
    print("✓ Added loadProductsAndAwards function")
else:
    print("✗ Could not find loadAwardRatings function")

