from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import re

path = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(path)
url = "https://10fastfingers.com/typing-test/english"
driver.get(url)


price = driver.find_element_by_xpath("//div[@id='wordlist']")
price_content = price.get_attribute('innerHTML')
listsend = price_content.split("|")

print(listsend)

for ele in listsend:
	notice=driver.find_element_by_id("inputfield")
	notice.send_keys(ele)
	notice.send_keys(" ")
	time.sleep(0.01)

print("done")


# cuối cùng thì t cũng xong rùi ^^