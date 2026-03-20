"""
 ### Title  
**Automate Resume Upload on Shine Registration Page**

### Description  
Open the Shine registration page using Selenium WebDriver (https://www.shine.com/registration/).  

Automate the process of uploading a resume file using Selenium.

Perform the following steps:
- Launch the browser and open the Shine registration page  
- Locate the **Upload Resume** file input field  
- Upload a resume file 


### Expected Outcome  
- The browser launches and opens the Shine registration page  
- Resume file is uploaded successfully  
- The uploaded file name is reflected in the UI  
- Script executes without errors  """

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.shine.com/registration/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[@name = 'resume_file'][1]").send_keys(r"C:\Desktop\capegemini\Kriti Jain Resume Updated.pdf")
sleep(3)
driver.quit()