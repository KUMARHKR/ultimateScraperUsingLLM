import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import re

def scrape_yellow_pages(base_url, num_pages):
    """Scrapes electrician data from Yellow Pages Australia, including website details.

    Args:
        base_url (str): The base URL of the search results.
        num_pages (int): The number of pages to scrape.

    Returns:
        pandas.DataFrame: A DataFrame containing the scraped data.
    """

    all_data = []  # Store all data in a list of dictionaries

    # Setup Selenium with Chrome WebDriver
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Uncomment for headless browsing
    driver = webdriver.Chrome(options=options)

    for page_num in range(1, num_pages + 1):
        url = f"{base_url}&pageNumber={page_num}"
        driver.get(url)

        # Wait for listings to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.MuiPaper-root"))
        )

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        for listing in soup.find_all('div', class_='MuiPaper-root'):
            electrician_data = {}  # Dictionary for each electrician

            name_element = listing.find('h3', class_='MuiTypography-h3')
            electrician_data['name'] = name_element.text.strip() if name_element else None

            rating_element = listing.find('div', class_='iiSpqr')
            electrician_data['rating'] = float(rating_element.text.strip()) if rating_element else None

            # # Extract review count
            # review_count_element = listing.find('p', class_='MuiTypography-body2', string=lambda text: text and "(" in text)
            # electrician_data['review_count'] = int(review_count_element.text.strip("()")) if review_count_element else None

            address_element = listing.find('p', class_='MuiTypography-body2', string=lambda text: text and "St" in text)
            electrician_data['address'] = address_element.text.strip() if address_element else None

            phone_element = listing.find('button', class_='ButtonPhone')

            if phone_element:
                phone_span = phone_element.find('span', class_='MuiButton-label')
                electrician_data['phone'] = phone_span.text.strip() if phone_span else None
            else:
                electrician_data['phone'] = None

            website_element = listing.find('a', class_='ButtonWebsite')
            website_url = website_element['href'] if website_element else None
            electrician_data['website'] = website_url

            # Extract data from the website (if a link is found)
            if website_url:
                try:
                    website_data = scrape_website(website_url)
                    electrician_data.update(website_data)  # Add website data to dictionary
                except Exception as e:
                    print(f"Error scraping {website_url}: {e}")

            all_data.append(electrician_data)

        print(f"Scraped page {page_num}")
        time.sleep(2)

    driver.quit()

    df = pd.DataFrame(all_data)
    return df

def scrape_website(url):
    """Scrapes business details from an electrician's website.

    Args:
        url (str): The website URL.

    Returns:
        dict: A dictionary containing the scraped website data.
    """
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')

    website_data = {}

    # Example: Find phone number using a regular expression
    phone_match = re.search(r'\(?\d{2,4}\)?\s?\d{3}\s?\d{3}', soup.get_text())
    website_data['website_phone'] = phone_match.group(0).strip() if phone_match else None

    # Example: Find email using a common pattern
    email_match = re.search(r'[\w\.-]+@[\w\.-]+', soup.get_text())
    website_data['email'] = email_match.group(0).strip() if email_match else None

    # TODO: Add more logic to find other website data (business name, address)
    # ... You'll need to adapt the code based on the website's structure ...

    return website_data


if __name__ == '__main__':
    # base_url = 'https://www.yellowpages.com.au/search/listings?clue=Electricians&locationClue=Australia' # Electricians
    base_url = 'https://www.yellowpages.com.au/search/listings?clue=Mechanic&locationClue=Australia' # Mechanics
    num_pages = 29

    df = scrape_yellow_pages(base_url, num_pages)
    print(df)
    df.to_csv('machanic_data_with_websites_main.csv', index=False)
