from selenium import webdriver
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import json

scrapFrom = "https://www.apartments.com/lansing-mi/"
pageIndex = 1
results = []

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-blink-features=AutomationControlled") 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
options.add_experimental_option("useAutomationExtension", False) 
driver = webdriver.Chrome(options=options) 
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 
useragentarray = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": useragentarray})

while True:
    print("start Scrapping from page" + str(pageIndex))
    driver.get(scrapFrom + str(pageIndex))
    articles = driver.find_elements(By.TAG_NAME, 'article')
    for article in articles:
        itemUrl = article.get_attribute('data-url')
        if itemUrl is not None:
            results.append(itemUrl)
    
    pageRange = int(driver.find_element(By.CSS_SELECTOR, 'span.pageRange').text.split('of')[1].strip())
    print("pageRange", pageRange)
    if pageIndex >= pageRange:
        break
    else:
        pageIndex += 1

with open('result.json', 'w') as file:
    file.write(json.dumps(results))

driver.close()