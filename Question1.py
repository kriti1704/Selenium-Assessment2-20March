""" ### Title

**Automate Data Extraction from Pro Kabaddi Standings**

### Description

Open the Pro Kabaddi website using Selenium WebDriver (https://www.prokabaddi.com/)
Navigate to the **Standings** section and locate the team **Jaipur Pink Panthers** in the points table.

Identify and extract the following details for the team:

* Matches Played
* Won
* Lost
* Score Difference (Diff)
* Points

Use appropriate locator strategies such as **XPath / CSS Selectors** to fetch the data dynamically from the table.

Students should ensure that:

* The browser opens successfully.
* Navigation to the standings page is completed.
* The correct team row (**Jaipur Pink Panthers**) is identified.
* All required values are extracted correctly.

### Expected Outcome

* The browser launches and opens the Pro Kabaddi website.
* The Standings page is displayed.
* The row corresponding to **Jaipur Pink Panthers** is located.
* Matches Played, Won, Lost, Diff, and Points are successfully fetched.
* The extracted values are printed in the console. """

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--headless")
driver = Chrome(options=o)
driver.get("https://www.prokabaddi.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//span[text()='Standings']").click()
matches_played = driver.find_element(By.XPATH,"//p[text()='Jaipur Pink Panthers']/../../../..//div[3]//p[1]")
print("Matches played:",matches_played.text)
won = driver.find_element(By.XPATH,"//p[text()='Jaipur Pink Panthers']/../../../..//div[4]//p[1]")
print("Won:",won.text)
lost = driver.find_element(By.XPATH,"//p[text()='Jaipur Pink Panthers']/../../../..//div[5]//p[1]")
print("Lost:",lost.text)
diff = driver.find_element(By.XPATH,"//p[text()='Jaipur Pink Panthers']/../../../..//div[6]//p[1]")
print("Diff:",diff.text)
points = driver.find_element(By.XPATH,"//p[text()='Jaipur Pink Panthers']/../../../..//div[8]//p[1]")
print("Points:",points.text)
driver.close()