import time
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Function to scrape data from a single page with WebDriverWait
def scrape_page_data(driver):
    '''
    # Wait until the table is present in the DOM
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header")))
    
    # Locate the table element
    table = driver.find_element(By.XPATH, '//*[@id="season-tabpanel"]/span/div/div[2]/table')

    rows = table.find_elements(By.TAG_NAME, "tr")
    
    data = []
    for row in rows:
        columns = row.find_elements(By.TAG_NAME, "td")
        row_data = [col.text for col in columns]
        data.append(row_data)
    '''

    # Locate the table element
    table = driver.find_element(By.XPATH, '//*[@id="season-tabpanel"]/span/div/div[2]/table')

    rows = table.find_elements(By.TAG_NAME, "tr")
    
    data = []
    for row in rows:
        columns = row.find_elements(By.TAG_NAME, "td")
        row_data = [col.text for col in columns]
        data.append(row_data)
    
    return data
    return data

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL of the NHL stats page
url_template = 'https://www.nhl.com/stats/skaters?aggregate=0&reportType=season&seasonFrom=20052006&seasonTo=20232024&gameType=2&status=active&sort=points,goals,assists&page={}&pageSize=100'

all_data = []
numPages = 56

# Loop through all pages (0 to 56)
for page in range(0, numPages+1):
    # Load the webpage
    driver.get(url_template.format(page))
    
    # Wait for the page to load
    time.sleep(5)  # Increase or decrease sleep depending on your internet speed
    
    # Scrape data from the current page
    page_data = scrape_page_data(driver)
    print(page)
    
    # Append the data to the full dataset
    all_data.extend(page_data)

# Define the maximum number of columns
max_columns = max(len(row) for row in all_data)

# Pad rows that have fewer columns
padded_data = [row + [None] * (max_columns - len(row)) for row in all_data]

# Convert the padded data into a NumPy array
data_np = np.array(padded_data)

# Now create the DataFrame
columns = ['Rank', 'Season', 'Player', 'Team', 'Skater Shoots', 'Player Position', 'Games Played', 'Goals', 'Assists', 'Points', 'Plus-Minus', 'Penalty in Minutes', 'Points Per Game Played', 'Even Strength Goals', 'Even Strength Points', 'Power Play Goals', 'Power Play Points', 'Shorthanded Goals', 'Shorthanded Points', 'Overtime Goals', 'Game Winning Goals', 'Shots', 'Shooting Percentage', 'Time on Ice per Game Played', 'Face-off Win Percentage']

df = pd.DataFrame(data_np, columns=columns)

# Save to CSV
df.to_csv('skater_stats.csv', index=False)

# Close the driver
driver.quit()