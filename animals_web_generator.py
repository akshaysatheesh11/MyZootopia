import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

def generate_html(animals_data):
    """Generates HTML for animal cards"""
    html = ""
    for animal in animals_data:
        html += '<li class="cards__item">'
        html += f'<div class="card__title">{animal.get("name", "Unknown Animal")}</div>'
        html += '<p class="card__text">'
        characteristics = animal.get("characteristics", {})
        
        # Add the diet
        html += f'<strong>Diet:</strong> {characteristics.get("diet", "Unknown")}<br>'
        
        # Add the locations
        locations = animal.get("locations", ["Unknown"])
        html += f'<strong>Location:</strong> {", ".join(locations)}<br>'
        
        # Add the type (from characteristics or direct field)
        animal_type = animal.get("type") or characteristics.get("type", "Unknown")
        html += f'<strong>Type:</strong> {animal_type}<br>'
        
        html += '</p></li>'
    
    return html

def write_html(html_content):
    """Inserts animal HTML into a template"""
    with open('animals_template.html', 'r') as template_file:
        template = template_file.read()
    
    # Replace placeholder with generated HTML content
    html_output = template.replace('__REPLACE_ANIMALS_INFO__', html_content)
    
    with open('animals.html', 'w') as output_file:
        output_file.write(html_output)

def main():
    # Load the animal data from the JSON file
    animals_data = load_data('animals_data.json')
    
    # Generate the HTML content for the animal cards
    html_content = generate_html(animals_data)
    
    # Write the generated HTML into a new file
    write_html(html_content)

if __name__ == "__main__":
    main()
