from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get(r"https://www.amazon.in/ref=nav_logo")
driver.maximize_window()

WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.TAG_NAME , "body"))
)

print("Page Title: ",driver.title)

all_elements = driver.find_elements(By.XPATH, "//*")
print("\nTotal number of objects on page:", len(all_elements))

links = driver.find_elements(By.TAG_NAME,"a")
images = driver.find_elements(By.TAG_NAME,"img")
divs = driver.find_elements(By.TAG_NAME,"div")
buttons = driver.find_elements(By.TAG_NAME,"button")
forms = driver.find_elements(By.TAG_NAME,"form")
inputs = driver.find_elements(By.TAG_NAME,"input")

print("\n--- Detailed Element Count ---")
print("Total Links:", len(links))
print("Total Images:", len(images))
print("Total Buttons:", len(buttons))
print("Total Inputs:", len(inputs))
print("Total Forms:", len(forms))
print("Total Divs:", len(divs))

print("\n--- Sample Link Texts ---")
for link in links:
    text = link.text.strip()
    if text:
        print(text)

time.sleep(10)
driver.quit()

