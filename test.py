from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import re

path = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(path)
url = "https://10fastfingers.com/typing-test/english"
driver.get(url)

time.sleep(3)

price = driver.find_element_by_xpath("//div[@id='wordlist']")
price_content = price.get_attribute('innerHTML')

listsend = price_content.split("|")
print(listsend)


for ele in listsend:
	notice=driver.find_element_by_id("inputfield")
	notice.send_keys(ele)
	notice.send_keys(" ")
	time.sleep(0.1)




# while(True):
# 	time.sleep(3)
# 	t = driver.find_element_by_id("reload-box")
# 	listsend = re.findall("[a-zA-Z]+",t.text)
# 	print(listsend)
# 	while(len(listsend) > 0):
# 		notice=driver.find_element_by_id("inputfield")
# 		notice.send_keys(listsend[0])
# 		notice.send_keys(" ")
# 		listsend.remove(listsend[0])
# 		time.sleep(0.1)




# art = main.find_element_by_xpath("//span[@wordnr='1']")


# count = 0
# for ele in listsend:
# 	notice=driver.find_element_by_id("inputfield")
# 	notice.send_keys(ele)
# 	notice.send_keys(" ")
# 	time.sleep(0.1)
# 	count += 1

# print(count)



# print(art.text)



# for i in range(10):
# a  = driver.find_elements_by_tag_name("body")
# print(a[0].text)

	# /span[@wordnr="0"]
	# '+ str(i) + '
# driver.get_element_by_xpath("//div[@class='price inlineBlock strong mediumText']").text

print("done")