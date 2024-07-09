from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


# Search query
find = "digital%20marketing%20manager"
file = 0

# loop through the pages
for i in range(1, 2):
    # Search for the query
    driver.get(f"https://www.yellowpages.com.au/search/listings?clue=Electricians&locationClue=Australia")

    try:
        elems = driver.find_elements(By.CLASS_NAME, "MuiButtonBase-root")
        print(f"Found {len(elems)} search results.")

        for p in range(1, 11):
            # Click on the profile
            try:
                profile = driver.find_element(By.XPATH, f'//li[{p}]/div/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a').click()
                # Click the contact info element
                contact_info_button = driver.find_element(By.XPATH, '//*[@id="top-card-text-details-contact-info"]').click()
                time.sleep(2)  # Wait for the contact info to load
                close = driver.find_element(By.XPATH, '//*[@id="ember2270"]').click()


                d = driver.page_source

                with open(f"data/{find}_{file}.html", "w", encoding="utf-8") as f:
                    f.write(d)
                    file += 1

                # Back to the main page
                driver.back()
                time.sleep(2)  # Wait for the main page to load

            except Exception as e:
                print(f"An error occurred: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Sleep for a while to view the results
time.sleep(1000)
driver.close()