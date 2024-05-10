import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC



url = "https://www.linkedin.com/jobs/search/?currentJobId=3888272646&keywords=machine%20learning%20engineer&origin=BLENDED_SEARCH_RESULT_NAVIGATION_SEE_ALL&originToLandingJobPostings=3908437257%2C3847173110%2C3918953192"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(10)


n = 800

i = 2
while i <= int((n+200)/25)+1: 
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        i = i + 1

        
        try:
            send=driver.find_element(By.XPATH, "//button[@aria-label='See more jobs']")
            driver.execute_script("arguments[0].click();", send)   
            time.sleep(3)
        except:
              time.sleep(5)

companyname= []
titlename= []
hrefList = []

try:
    for i in range(n):
        company=driver.find_elements(By.CLASS_NAME, 'base-search-card__subtitle')[i].text
        companyname.append(company)
        
            
except IndexError:
    print("no")


try:
    for i in range(n):
        title=driver.find_elements(By.CLASS_NAME, 'base-search-card__title')[i].text
        titlename.append(title)
        
            
except IndexError:
    print("no")
        

        
companyfinal=pd.DataFrame(companyname,columns=["company"])
titlefinal=pd.DataFrame(titlename,columns=["title"])
#hreffinal=pd.DataFrame(hrefList,columns=["Link"])

x=companyfinal.join(titlefinal)
#full = x.join(hreffinal)
x.to_csv('linkedin.csv')
