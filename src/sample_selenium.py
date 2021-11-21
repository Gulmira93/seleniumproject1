from selenium import webdriver

# 1. open the browser
driver = webdriver.Chrome()
driver.implicitly_wait(20)
# driver is object , any word we can use instead of it like browser
# here get is function to open browser, it gets request to this following URL
driver.get("https://www.thelevelupsolutions.com/")

driver.maximize_window()















