import 'dotenv/config'
import axios from 'axios';
import jsdom from "jsdom";
import { Readability } from '@mozilla/readability';
import fs from 'fs';


// Get the API key from the environment variables
const apiKey = process.env.NEWS_API_KEY;
const outPath = process.env.OUT || `dump-${new Date().toISOString()}.json`;

// Calculate the date range for the past week
const now = new Date();
const weekAgo = new Date(now.getTime() - 7 * 24 * 60 * 60 * 1000);
const from = weekAgo.toISOString().split('T')[0];
const to = now.toISOString().split('T')[0];
const language='en'
const q='news'

// Make the API request
let url = 'https://newsapi.org/v2/everything';
const params = { apiKey, from, to, language, q};

const queryString = new URLSearchParams(params).toString();
url = `${url}?${queryString}`;

let response = await axios.get(url);

if (response.status != 200) {
    console.error("error during the request to newsapi");
}

let dataset = [];
const toawait = 50;
for (const article of response.data.articles) {
    
    await new Promise((resolve) => setTimeout(resolve, toawait));
    try {
        let articleResponse = await axios.get(article.url);
        if (articleResponse.status != 200) {
            console.error("error during the request to ", article.title);
            continue;
        }
    
        let dom = new jsdom.JSDOM(articleResponse.data, {
            url: article.url
        });
    
        let articleContent = new Readability(dom.window.document).parse();
        if (articleContent.textContent.startsWith("Opening")){
            continue;    
        }

        let articleInfo = {
            url : article.url,
            title :  article.title,
            urlToImage : article.urlToImage,
            data : article.publishedAt,
            content : articleContent.textContent
        };

        dataset.push(articleInfo)

    } catch (error) {
        console.error("error during the request to ", article.title);
        continue;
    }
}

fs.writeFileSync(outPath, JSON.stringify(dataset));
