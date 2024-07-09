# This is a Project Ultime Web Scaper Using LLM models.
# This is a web scaper that will scrape the web for information and store it in a database.
# Author: Dip Kumar Dhawa
# Language: Python
# Libraries: requests, Selenium , BeautifulSoup, pandas, numpy, LLM, ect.
# Models: LLM ( GPT , grok , Gemini pro ect.)


from bs4 import BeautifulSoup
import selenium as sl
import requests as rq
import pandas as pd
import numpy as np
import tkinter as tk
import os, time
import nest_asyncio

from llm_config import get_graph_config



graph_config = get_graph_config()
nest_asyncio.apply()
from scrapegraphai.graphs import SmartScraperGraph

smart_scraper_graph = SmartScraperGraph(
    # prompt="The list must include ,Phone Numbers (Australian customers) ,Business Emails (matching with customer phone numbers) , Business name, Phone Number, Website, Email, address.",
    prompt= "All Detales List",
    source="https://www.upwork.com/freelance-jobs/data-science/",
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)

# # Save to a Data Frame
# df = pd.DataFrame(result['output'])
# df.to_csv('data/anime.csv', index=False)




