
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 1. open the browser
driver = webdriver.Chrome()
driver.implicitly_wait(20)  # synchronizing the browser
driver.maximize_window()

# 2. open the automationpractice.com demo website
driver.get("http://automationpractice.com/index.php")

# xpath: https://www.guru99.com/xpath-selenium.html
# //ul[@id='homefeatured']//a[@class='product-name' and @title='Blouse']
# //ul[@id='homefeatured']
# //a[@title='Women']  - finding using attribute in the xpath
# //a[text()='Ladies'] - finding using text of the element in your xpath
# //b[text()='Cart']
# //ul[@class="sf-menu clearfix menu-content sf-js-enabled sf-arrows"]/li[2]
search_box = driver.find_element(By.XPATH, "//input[@id='search_query_top']")
# search_box = driver.find_element(By.ID, "search_query_top")
search_box.send_keys('dress' + Keys.ENTER)
# search_box.send_keys('dress')
# search_box.send_keys(Keys.ENTER)

# css selector: https://www.guru99.com/locators-in-selenium-ide.html
# ul#homefeatured a.product-name[title='Blouse']
# //ul[@id='homefeatured'] vs ul#homefeatured
# //a[@title='Women']  vs a[title='Women']
# //a[text()='Ladies'] vs a:contains('Ladies')
time.sleep(5)
result = driver.find_element(By.CSS_SELECTOR, 'span.heading-counter').text
print("result of the search", result)
print("###### Example for find elements#########")

products = driver.find_elements(By.XPATH, "//div[@id='center_column']//a[@class='product-name']")
#nums = [2, 3, 4, 5, 6]
product_names = []
for product in products: # identify each element in a list
   print(f"'{product.text}'")
   product_names.append(product.text.strip())  # append is saving product names. strip rids off white spaces
print(product_names)






print("------------- Completed --------------------")
# find_element vs find_elements
# results = driver.find_elements(By.CSS_SELECTOR, 'span.heading-counter')
# above will return elements in a list
# please be aware of this you will get following Error:
# AttributeError: 'list' object has no attribute 'text'

time.sleep(5)
# locators: id, name, class, >> xpath, css selector  >> link_text,
driver.quit()

