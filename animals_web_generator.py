import data_fetcher

def generate_html(animals_data):
    """generates HTML for animal cards"""
    html = ""
    for animal in animals_data:
        if 'error' in animal:
            html += f"<h2>{animal['name']} doesn't exist or an error occurred: {animal['error']}</h2>"
        else:
            html += '<li class="cards__item">'
            html += f'<h2>{animal.get("name", "Unknown Animal")}</h2>'
            html += '<p class="cards__text">'
            characteristics = animal.get("characteristics", {})
            html += f'<strong>Diet:</strong> {characteristics.get("diet", "Unknown")}<br>'
            html += f'<strong>Location:</strong> {animal.get("locations", ["Unknown"])[0]}<br>'
            animal_type = animal.get("type") or characteristics.get("type", "Unknown")
            html += f'<strong>Type:</strong> {animal_type}<br>'
            html += '</p></li>'
    return html


def write_html(html_content):
    """inserts animal HTML into a template"""
    with open('animals_template.html', 'r') as template_file:
        template = template_file.read()
    html_output = template.replace('__REPLACE_ANIMALS_INFO__', html_content)
    with open('animals.html', 'w') as output_file:
        output_file.write(html_output)


def main():
    animal_name = input("Please enter an animal: ")
    animals_data = data_fetcher.fetch_data(animal_name)
    html_content = generate_html(animals_data)
    write_html(html_content)


if __name__ == "__main__":
    main()