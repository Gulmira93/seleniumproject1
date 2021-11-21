# Title of the page
##Title 2 of the page
### title 3

# Selenium WebDriver with Python

## Selenium setup
1. download selenium
  go to the (Terminal (pycharm)
  '''python
  pip install selenium # library , code written by developers open source
  pip freeze # checking the selenium is in the list 
  '''
2. download chromedriver
   - check the version of your chrome browser (if you dont have chrome browser,
     download and install it)
       - download chrome driver from this location: [driver website]
         (https://chromedriver.storage.googleapis.com/index.html?path=95.0.4638.54/)
3. save in the Python main location
   - go to the python main folder: "C:/Program Files/python39"
    - paste the copied chromedriver here 
4. import selenium, run sample code

## what is html?

- Document object model - html documenr (DOM)
- tag  :
   head, body, div,button, span,a (links), input(text, password,
  submit, checkbox (radio,))
  
### Using chrome  Developer tools options to inspect web elements
- Tags are purple
- Attributes are red
- values of the attributes will be in blue
- text in the elements, that are in black

H/W : read and try out html documents
- https://www.w3schools.com/html/html_intro.asp
- https://www.w3schools.com/html/html_elements.asp
- https://www.w3schools.com/html/html_attributes.asp 
- https://www.w3schools.com/html/html_links.asp
- https://www.w3schools.com/html/html_forms.asp

### Finding the element
```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(20)  
driver.maximize_window()

driver.get("https://www.google.com/")
# 3. search for 'selenium'
driver.find_element_by_id()  # fastest way of finding element from html document
driver.find_element_by_name()

driver.find_element_by_xpath() # technics , build . like file path
driver.find_element_by_css_selector() # technics, build (it is like file path)

driver.find_element_by_link_text()
driver.find_element_by_class_name() #Class names might be dynamic


driver.find_element_by_partial_link_text()
driver.find_elements_by_tag_name()

```

- webdriver - handling web browser

- webelement - working with element

- framework - manage the code better





