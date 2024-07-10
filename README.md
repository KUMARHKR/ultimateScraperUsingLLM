### Project Title: Web Scraping for Business Data Extraction

### Description:

**Objective:**
The goal of this project is to develop a robust web scraping solution that extracts detailed business information from Yellow Pages Australia. This project specifically targets data extraction for electricians and mechanics, focusing on gathering comprehensive details, including website data.

**Project Overview:**
In this project, I implemented a web scraper using Python, BeautifulSoup, and Selenium. The scraper navigates through multiple pages of search results on Yellow Pages Australia, extracting key information about each business listing. To enhance the dataset, the scraper also visits individual business websites to gather additional details.

**Key Features:**
1. **Selenium Integration**: Utilized Selenium for dynamic web page interaction and automated browsing, ensuring the extraction of data from pages with JavaScript-rendered content.
2. **BeautifulSoup Parsing**: Employed BeautifulSoup for efficient HTML parsing and data extraction from the web pages.
3. **Data Points Collected**:
   - **Business Name**
   - **Rating**
   - **Address**
   - **Phone Number**
   - **Website URL**
4. **Website Data Extraction**: Developed a function to scrape business websites for additional contact details such as phone numbers and email addresses.
5. **Handling Class Imbalance**: Addressed the common issue of class imbalance in datasets by implementing SMOTE (Synthetic Minority Over-sampling Technique) to create a balanced dataset, ensuring the model can effectively learn from both legitimate and fraudulent transactions.
6. **Data Storage**: Collected data was stored in a pandas DataFrame and exported to a CSV file for further analysis and model training.

**Technologies Used:**
- Python
- Selenium
- BeautifulSoup
- pandas
- requests
- re (regular expressions)

**Challenges Addressed:**
- **Class Imbalance**: Applied resampling techniques to handle the imbalanced dataset problem commonly faced in fraud detection.
- **Dynamic Content Loading**: Used Selenium to manage and interact with dynamically loaded web content, ensuring comprehensive data extraction.
- **Data Cleaning and Validation**: Implemented robust data cleaning and validation steps to ensure the accuracy and quality of the extracted data.

**Outcome:**
The project successfully scraped and compiled a detailed dataset of business listings, including enriched data from business websites. This dataset can be utilized for various applications, such as fraud detection models, market analysis, and business intelligence.
