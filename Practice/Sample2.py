from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Start browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open HTML file
driver.get(r"file:///D:/Choco/STQA/Assignment10/dropdown.html")

# Wait for page load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "body"))
)

# -------------------------------
# Count items in dropdown
# -------------------------------
dropdown = driver.find_elements(By.XPATH, "//select[@id='courses']/option")
print("Number of items in dropdown:", len(dropdown))

# -------------------------------
# Count items in list
# -------------------------------
list_items = driver.find_elements(By.XPATH, "//ul[@id='cityList']/li")
print("Number of items in list:", len(list_items))

time.sleep(10)

# Close browser
driver.quit()

