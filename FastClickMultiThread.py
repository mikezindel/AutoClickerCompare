#fast
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import threading

#cookie clicker https://orteil.dashnet.org/cookieclicker/
#click test     https://clickspeedtest.com/5-seconds.html
path_to_extension = r'C:\Users\susan\Documents\1.34.0_22'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome("C:\chromedriver.exe" ,chrome_options=chrome_options)
driver.create_options()
driver.get("https://orteil.dashnet.org/cookieclicker/")
id = driver.find_element_by_id('bigCookie')



def do_request():
    while True: # click for ever
      try:
        id.click()
      except Exception as ex: # until it breaks
        break

threads = []

for i in range(50): #too many threads does not scale properly 
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()

time.sleep(1) # results are slow
result = driver.find_element_by_css_selector('.times')
print(f'Result: {result.text}\n')
driver.close()
