import json
from datetime import datetime
import math


def getStars(number: float):
    stars = math.floor(number)
    startsHtml = """
        <div class="flex items-center space-x-1">
    """
    for _ in range(0,stars):
        startsHtml +="""
            <svg class="w-4 h-4 text-yellow-300" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 22 20">
                <path d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"/>
            </svg>
        """

    for _ in range(5-stars):
        startsHtml +="""
            <svg class="w-4 h-4 text-gray-300 dark:text-gray-500" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 22 20">
                <path d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"/>
            </svg>
        """
    startsHtml +="""
        </div>
    """

    return startsHtml
    

def generate_journal(json_file):
    # Read the JSON data from file
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Group entries by category
    grouped_entries = {}
    grouped_max = {}
    for entry in data:
        category = entry['category']
        if not category in grouped_entries:
            grouped_entries[category] = [entry]
            grouped_max[category] = entry["urls_found"]
            continue
        grouped_entries[category].append(entry)
        grouped_max[category] = entry["urls_found"] if entry["urls_found"] > grouped_max[category] else grouped_max[category]
    

    # Create the HTML string
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>IntelliNews</title>
        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
        <script src="https://cdn.tailwindcss.com?plugins=forms,typography,aspect-ratio,line-clamp"></script>
        <link href="https://cdnjs.cloudflare.com/ajax/libs/flowbite/1.7.0/flowbite.min.css" rel="stylesheet" />

    </head>
    <body class="my-24">
        <aside id="default-sidebar" class="hidden lg:block fixed top-0 left-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0" aria-label="Sidebar">
            <div class="h-full px-3 py-4 overflow-y-auto bg-stone-50">
                <h1 class="p-2 mt-8 mb-16 text-stone-900 font-extrabold text-xl sm:text-2xl lg:text-3xl tracking-tight">IntelliNews</h1>
                <p class="p-2 my-4">Sections</p>
                <ul class="space-y-2 font-medium">
                    '''
    
    for category, entries in grouped_entries.items():
        html += '''
            <li>
                <a href="#cat-{}" class="text-blue-500 hover:underline flex items-center p-2">
                    <span class="ml-3">{}</span>
                </a>
            </li>
            '''.format(category,category)
        
    html+= '''
                </ul>
        </div>
    </aside>

        <div class="prose prose-stone lg:prose-xl mx-auto md:px-3">
    '''

    # Generate the journal entries for each category
    for category, entries in grouped_entries.items():
        html += '''
        <div>
            <span class="my-4" id="cat-{}">&nbsp;</span>
            <h1 class="text-center text-2xl font-bold">{}</h1>
            <hr class="my-4">
        '''.format(category, category)

        for entry in entries:
            val = math.floor((entry["urls_found"] / grouped_max[category]*5)*10)/10
            if val > 5:
                val = 5
            
            html += '''
            <div>
                <h2 class="font-black">{}</h2>
                <div class="flex items-center space-x-2">
                    <p class="text-sm text-stone-500">{}</p>
                    <p class="text-sm text-stone-500">|</p>
                    <p class="text-sm text-stone-500">Relevance:</p>
                    {}
                    <p class="text-sm text-stone-500">{}/5</p>
                </div>
                <img src="{}" alt="Image" class="my-4 max-w-lg mx-auto rounded">
                <p>{}</p>
                <a href="{}" class="text-blue-500 hover:underline">Read More</a>
                <hr class="my-8">
            </div>
            '''.format(
                entry['title'],     
                datetime.strptime(entry['date'], "%Y-%m-%dT%H:%M:%SZ").strftime("%B %d, %Y"),
                getStars(val),
                val,
                entry['urlToImage'], 
                entry['summary'], 
                entry['url'],
                entry["urls_found"],
            )
        html += '''
        </div>
        '''

    # Complete the HTML string
    html += '''
        </div>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/flowbite/1.7.0/flowbite.min.js"></script>
    </body>
    </html>
    '''

    return html

# Example usage
json_file = 'data/final-final.json'  # Replace with the path to your JSON file
html = generate_journal(json_file)
print(html)
