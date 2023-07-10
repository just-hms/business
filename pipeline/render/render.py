import json

def generate_journal(json_file):
    # Read the JSON data from file
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Create the HTML string
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Journal</title>
        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
        <style>
            .prose {
                max-width: 48rem;
                margin-left: auto;
                margin-right: auto;
                padding: 1rem;
            }
        </style>
    </head>
    <body>
        <div class="prose">
    '''

    # Generate the journal entries
    for entry in data:
        html += '''
        <div>
            <h2 class="text-xl font-bold">{}</h2>
            <p class="text-sm text-gray-500">{}</p>
            <img src="{}" alt="Image" class="my-4 rounded">
            <p>{}</p>
            <a href="{}" class="text-blue-500 hover:underline">Read More</a>
            <hr class="my-8">
        </div>
        '''.format(entry['article'], entry['date'], entry['urlToImage'], entry['summary'], entry['url'])

    # Complete the HTML string
    html += '''
        </div>
    </body>
    </html>
    '''

    return html

# Example usage
json_file = 'data.json'  # Replace with the path to your JSON file
html = generate_journal(json_file)
print(html)
