from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(20)
# driver is object , any word we can use instead of it like browser
# here get is function to open browser, it gets request to this following URL
#driver.get("https://www.thelevelupsolutions.com/")
# 1. open the browser
driver.maximize_window()
driver.get("http://automationpractice.com/index.php")