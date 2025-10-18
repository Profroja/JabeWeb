(function() {
    function loadSubcategories(categoryId) {
        var subcategorySelect = document.getElementById('id_subcategory');
        
        if (categoryId && subcategorySelect) {
            // Disable the select while loading
            subcategorySelect.disabled = true;
            
            var xhr = new XMLHttpRequest();
            xhr.open('GET', '/admin/products/product/get-subcategories/?category_id=' + categoryId, true);
            xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
            
            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4) {
                    subcategorySelect.disabled = false;
                    
                    if (xhr.status === 200) {
                        try {
                            var data = JSON.parse(xhr.responseText);
                            
                            // Clear existing options
                            subcategorySelect.innerHTML = '<option value="">---------</option>';
                            
                            // Add new options
                            for (var i = 0; i < data.length; i++) {
                                var option = document.createElement('option');
                                option.value = data[i].id;
                                option.textContent = data[i].name;
                                subcategorySelect.appendChild(option);
                            }
                        } catch (e) {
                            console.error('Error parsing JSON:', e);
                            subcategorySelect.innerHTML = '<option value="">---------</option>';
                        }
                    } else {
                        subcategorySelect.innerHTML = '<option value="">---------</option>';
                    }
                }
            };
            
            xhr.send();
        } else if (subcategorySelect) {
            subcategorySelect.innerHTML = '<option value="">---------</option>';
        }
    }

    function initSubcategoryFilter() {
        var categorySelect = document.getElementById('id_category');
        var subcategorySelect = document.getElementById('id_subcategory');
        
        if (categorySelect && subcategorySelect) {
            // Clear subcategory options initially
            subcategorySelect.innerHTML = '<option value="">---------</option>';
            subcategorySelect.value = '';
            
            // Handle category change
            categorySelect.addEventListener('change', function() {
                var categoryId = this.value;
                if (categoryId) {
                    loadSubcategories(categoryId);
                } else {
                    // Clear subcategory if no category selected
                    subcategorySelect.innerHTML = '<option value="">---------</option>';
                    subcategorySelect.value = '';
                }
            });
            
            // Handle form submission - clear subcategory if no category
            var form = document.querySelector('form');
            if (form) {
                form.addEventListener('submit', function() {
                    if (!categorySelect.value) {
                        subcategorySelect.value = '';
                    }
                });
            }
            
            // Load initial subcategories if category is already selected
            if (categorySelect.value) {
                loadSubcategories(categorySelect.value);
            }
        }
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initSubcategoryFilter);
    } else {
        initSubcategoryFilter();
    }
})();
