import json
from datetime import datetime

def generate_journal(json_file):
    # Read the JSON data from file
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Group entries by category
    grouped_entries = {}
    for entry in data:
        category = entry['category']
        if category in grouped_entries:
            grouped_entries[category].append(entry)
        else:
            grouped_entries[category] = [entry]

    # Create the HTML string
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>IntelliNews</title>
        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
        <script src="https://cdn.tailwindcss.com?plugins=forms,typography,aspect-ratio,line-clamp"></script>
    </head>
    <body class="my-32">
        <div class="prose prose lg:prose-xl mx-auto px-3">
    '''

    # Generate the journal entries for each category
    for category, entries in grouped_entries.items():
        html += '''
        <div>
            <h1 class="text-center text-2xl font-bold">{}</h1>
            <hr class="my-4">
        '''.format(category)

        for entry in entries:
            html += '''
            <div>
                <h2>{}</h2>
                <p class="text-sm text-gray-500">{}</p>
                <img src="{}" alt="Image" class="my-4 max-w-lg mx-auto rounded">
                <p>{}</p>
                <a href="{}" class="text-blue-500 hover:underline">Read More</a>
                <hr class="my-8">
            </div>
            '''.format(
                entry['title'],     
                datetime.strptime(entry['date'], "%Y-%m-%dT%H:%M:%SZ").strftime("%B %d, %Y"),
                entry['urlToImage'], 
                entry['summary'], 
                entry['url'],
            )

        html += '''
        </div>
        '''

    # Complete the HTML string
    html += '''
        </div>
    </body>
    </html>
    '''

    return html

# Example usage
json_file = 'data/final-with-weight.json'  # Replace with the path to your JSON file
html = generate_journal(json_file)
print(html)
