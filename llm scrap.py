# This is a Project Ultime Web Scaper Using LLM models.
# This is a web scaper that will scrape the web for information and store it in a database.
# Author: Dip Kumar Dhawa
# Language: Python
# Libraries: requests, Selenium , BeautifulSoup, pandas, numpy, LLM, ect.
# Models: LLM ( GPT , grok , Gemini pro ect.)

from scrapegraphai.graphs import SmartScraperGraph
from dotenv import load_dotenv
import os
load_dotenv()

import nest_asyncio
nest_asyncio.apply()

# Retrieve the API key from the environment
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

graph_config = {
    "llm": {
        "api_key": GOOGLE_API_KEY,
        "model": "gemini-pro",
    },
    "verbose":True
}

smart_scraper_graph = SmartScraperGraph(
    prompt=" Business name, Phone Number, Website, Email, address",
    # also accepts a string with the already downloaded HTML code
    source="https://njbelectrical.com.au/",
    config=graph_config
)

result = smart_scraper_graph.run()

import json

output = json.dumps(result, indent=2)

line_list = output.split("\n")  # Sort of line replacing "\n" with a new line

for line in line_list:
    print(line)


#%%
