import spacy
from serpapi import GoogleSearch
from dotenv import load_dotenv

import os

load_dotenv()

nlp = spacy.load("en_core_web_sm")

text = """spaCy is an open-source software library for advanced natural language processing, 
written in the programming languages Python and Cython. The library is published under the MIT license
and its main developers are Matthew Honnibal and Ines Montani, the founders of the software company Explosion."""

doc = nlp(text)

kek = []
for x in doc.ents:
    kek.append(x.root.__str__())

print(kek)

params = {
  "engine": "google_trends",
  "q": kek,
  "data_type": "TIMESERIES",
  "api_key": os.getenv("SERPAPI_KEY")
}

search = GoogleSearch(params)
results = search.get_dict()
interest_over_time = results["interest_over_time"]
