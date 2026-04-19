from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get(r"file:///D:/Choco/STQA/Assignment10/dropdown.html")
driver.maximize_window()

WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.TAG_NAME,"body"))
)

dropdown = driver.find_elements(By.XPATH,"//select[@id ='courses']/option")
print("No. of items in Dropdwon on Webpage: ",len(dropdown))

list_items = driver.find_elements(By.XPATH,"//ul[@id ='cityList']/li")
print("No. of items in list on Webpage: ",len(list_items))

time.sleep(5)

driver.quit()