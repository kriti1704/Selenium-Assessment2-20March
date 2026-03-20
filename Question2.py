""" ### Title  
**Automate SauceDemo Login and Product Page with Explicit Waits and Verification**

### Description  
Open the SauceDemo website using Selenium WebDriver (https://www.saucedemo.com/).  

Implement the login flow and product page interactions using **Explicit Waits** to ensure elements are properly loaded and interactable.

Perform the following steps:
- Wait for the **Username** field to be clickable and enter `"standard_user"`  
- Wait for the **Password** field to be clickable and enter `"secret_sauce"`  
- Wait for the **Login** button to be clickable and click on it  
- After login, wait for the **Products title** to be visible  
- Capture and print the page title text  

Continue with product page actions:
- Find ALL product names and print each name  
- Find ALL product prices and print each price  
- Click on the fourth product’s **Add to cart** button  
  

Use **WebDriverWait** along with **Expected Conditions** for synchronization.

Students should ensure that:
- Explicit waits are used for each interaction step  
- No `sleep()` is used in the script  
- At least **2 different locator strategies** are used (ID, CSS Selector, XPath, Class Name, etc.)  
- Proper comments are added explaining locator usage  

### Expected Outcome  
- The browser launches and opens the SauceDemo website  
- Login is performed successfully using explicit waits  
- The **"Products"** page is displayed after login  
- Page title is printed as **Products**  
- All product names and prices are printed in the console  
- First product is added to cart   
- Script executes without timing issues """

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--disable-notifications")
driver = Chrome(options=o)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
wait = WebDriverWait(driver,10)

# Login
wait.until(EC.element_to_be_clickable((By.ID,"user-name"))).send_keys("standard_user")
wait.until(EC.element_to_be_clickable((By.ID,"password"))).send_keys("secret_sauce")
wait.until(EC.element_to_be_clickable((By.ID,"login-button"))).click()

# printing the title
title = wait.until(EC.visibility_of_element_located((By.XPATH,"//span[text()='Products']")))
print(title.text)

# fetching product names and prices
products = driver.find_elements(By.XPATH,"//div[@class='inventory_item_name ']")
prices = driver.find_elements(By.XPATH,"//div[@class='pricebar']//div")
print("Product names and Prices:")
for i in range(len(products)): 
    print(products[i].text,"=",prices[i].text)

# adding the 4th product in the cart
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))).click()
driver.close()
