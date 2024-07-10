import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

def scrape_yellow_pages(base_url, num_pages):
    """Scrapes data from Yellow Pages Australia for multiple pages.

    Args:
        base_url (str): The base URL of the search results.
        num_pages (int): The number of pages to scrape.

    Returns:
        pandas.DataFrame: A DataFrame containing the scraped data.
    """

    # Initialize lists to store data
    all_names = []
    all_ratings = []
    all_addresses = []
    all_phones = []
    all_websites = []

    # Setup Selenium with Chrome WebDriver
    options = webdriver.ChromeOptions()
    # Add arguments if needed, e.g., options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    for page_num in range(1, num_pages + 1):
        url = f"{base_url}&pageNumber={page_num}"
        driver.get(url)

        # Wait for listings to load (adjust the timeout as needed)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.MuiPaper-root"))
        )

        # Get the page source after JavaScript rendering
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # Extract data using Beautiful Soup
        for listing in soup.find_all('div', class_='MuiPaper-root'):
            name_element = listing.find('h3', class_='MuiTypography-h3')
            name = name_element.text.strip() if name_element else None

            rating_element = listing.find('div', class_='iiSpqr')
            rating = float(rating_element.text.strip()) if rating_element else None

            address_element = listing.find('p', class_='MuiTypography-body2', string=lambda text: text and "St" in text)
            address = address_element.text.strip() if address_element else None

            phone_element = listing.find('button', class_='ButtonPhone', string=lambda text: text and "(" in text)
            phone = phone_element.text.strip() if phone_element else None

            website_element = listing.find('a', class_='ButtonWebsite')
            website = website_element['href'] if website_element else None

            all_names.append(name)
            all_ratings.append(rating)
            all_addresses.append(address)
            all_phones.append(phone)
            all_websites.append(website)

        print(f"Scraped page {page_num}")
        time.sleep(2)  # Be polite: add a delay between page requests

    # Close the browser
    driver.quit()

    # Create a DataFrame
    df = pd.DataFrame({
        'Name': all_names,
        'Rating': all_ratings,
        'Address': all_addresses,
        'Phone': all_phones,
        'Website': all_websites
    })

    return df

if __name__ == '__main__':
    base_url = 'https://www.yellowpages.com.au/search/listings?clue=Electricians&locationClue=Australia'
    num_pages = 10

    df = scrape_yellow_pages(base_url, num_pages)
    print(df)
    df.to_csv('electricians_data.csv', index=False)