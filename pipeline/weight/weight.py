import datetime
from googlesearch import search, get_tbs

import time
import random
import yake
import spacy
import json

# Read the JSON file
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

nlp = spacy.load("en_core_web_sm")
kw_extractor = yake.KeywordExtractor(top=10, stopwords=None)
nlp = spacy.load("en_core_web_sm")

for obj in data:
    val = obj["summary"]

    keywords = kw_extractor.extract_keywords(val)[:1]

    doc = nlp(val)

    keywords.append(
        [ent.text.lower() for ent in doc.ents if ent.label_ in ['PERSON', 'ORG', 'GPE']][:2]
    )


    query = ""
    for x in keywords:
        query += (" " + x[0]) if len(x) > 0 else ""

    print(query)
    
    url_count=0
    for url in search(
        query, 
        num=20,
        start=0,
        pause=0.5,
        stop=None,
        tbs=get_tbs(
            datetime.date.today(),
            datetime.date.today() - datetime.timedelta(days=7)
        )
    ):
        time.sleep(random.randint(3,9)/200)
        url_count += 1

    time.sleep(random.randint(1,3))
    obj["urls_found"] = url_count
    print("found urls:", url_count)

# Write the updated data back to the JSON file
with open('output.json', 'w') as file:
    json.dump(data, file)
