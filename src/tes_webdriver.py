from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(20)
# driver is object , any word we can use instead of it like browser
# here get is function to open browser, it gets request to this following URL
#driver.get("https://www.thelevelupsolutions.com/")
# 1. open the browser
driver.maximize_window()
driver.get("http://automationpractice.com/index.php")


## xpath: https://www.guru99.com/xpath-selenium.html
#//ul@id='homefeatured']//a@class='product-name' and @title ='Blouse']
##//ul@id='homefeatured']
# ul#homefeatured a.product-name[title='Blouse']
# c

#//a[@title='women' vs a[title= 'women']  - finding using attribute in the xpath
#//a [text()='ladies']- finding using text of the element in your xpath
# //b[text()= 'Cart']
#//ul@class="sf-menu clearfix menu-content sf-js-enabled sf-arrows"]/li[2]

search_box= driver.find_element(By.XPATH, "//input[@id='search_query_top']")
search_box= driver.find_element(By.ID, "'search_query_top']")
search_box.send_keys('dress' + Keys.ENTER)

#search_box.send_keys('dress')
# search_box.send_keys(Keys.ENTER)

# css selector: http://www.guru99.com/locators-in-selenium-ide.html
#ul#homefeatured a.product-name[title='blouse']
#//ul[@id='homefeatured'] vs ul#homefeatured - css selector second one
# //a[@title='Women'] vs a[title='women']
# //a[@text()='women'] vs a:contains('Ladies')
time.sleep(5)
# css - comes without // and @
result = driver.find_element(BY.CSS_SELECTOR, 'span.heading-counter').text
print("######################result of search", result)
print('##########Find element examples')















print("--------------Completed-----------")
time.sleep(5)
# locators: id,
driver.quit()





