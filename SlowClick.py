#selenium clicker py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

path_to_extension = r'C:\Users\susan\Documents\1.34.0_22'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome("C:\chromedriver.exe" ,chrome_options=chrome_options) #loads chromedriver and adblock
driver.create_options()
driver.get("https://clickspeedtest.com/5-seconds.html")
id = driver.find_element_by_id("clicker")

actions = ActionChains(driver) #queues actions causing a much slower clickrate
actions.click(id)

while True: # click for ever
  try:
    actions.perform()
  except Exception as ex: # until it breaks
    break

time.sleep(1) # results are slow
result = driver.find_element_by_css_selector('.times')
print(f'Result: {result.text}\n')
driver.close()
