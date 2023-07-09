INSTRUCTIONS:
- The code expects a json file formatted as jsonlines called news.json
- Make sure the json, the vectorizer and the classifier pickle files are in the same folder as the .py executable
- The program produces a news_elaborated.json file formatted AS A STANDARD JSON
- The classes of each element are:
        {
            "article": "[the full original article]",
            "url": "[the url]",
            "urlToImage": "[url to the image]",
            "date": "[date of the article]",
            "category": "[the result of the category classification]",
            "summary": "[the summary provided by chatGPT]"
        },
