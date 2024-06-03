from selenium import webdriver 
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import time 
 
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

url = 'https://debank.com/profile/0xa7888f85bd76deef3bd03d4dbcf57765a49883b3'
driver.get(url)

time.sleep(7)

wait = WebDriverWait(driver, 3)

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.Portfolio_projectsShowAll__Huhry'))).click()

element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.HeaderInfo_totalAssetInner__HyrdC.HeaderInfo_curveEnable__HVRYq')))
print('Product name: ' + element.text)

container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.Portfolio_projectGrid__dT8a4')))

tokenEles = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.ProjectCell_assetsItemWrap__cvidP')))
for tokenEle in tokenEles:
    print(tokenEle.text)

driver.close()