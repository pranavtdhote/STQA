from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Start browser (VISIBLE mode)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open your HTML file (use RAW STRING for space path)
driver.get(r"file:///D:/Choco/STQA/Assignment9/sample.html")

# Wait until page loads properly
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "body"))
)

# -------------------------------
# DEBUG: confirm correct page
# -------------------------------
print("Page Title:", driver.title)

# -------------------------------
# 1. Count ALL elements
# -------------------------------
all_elements = driver.find_elements(By.XPATH, "//*")
print("\nTotal number of objects on page:", len(all_elements))

# -------------------------------
# 2. Count specific elements
# -------------------------------
links = driver.find_elements(By.TAG_NAME, "a")
images = driver.find_elements(By.TAG_NAME, "img")
buttons = driver.find_elements(By.TAG_NAME, "button")
inputs = driver.find_elements(By.TAG_NAME, "input")
forms = driver.find_elements(By.TAG_NAME, "form")
divs = driver.find_elements(By.TAG_NAME, "div")

print("\n--- Detailed Element Count ---")
print("Total Links:", len(links))
print("Total Images:", len(images))
print("Total Buttons:", len(buttons))
print("Total Inputs:", len(inputs))
print("Total Forms:", len(forms))
print("Total Divs:", len(divs))

# -------------------------------
# 3. Print visible link texts
# -------------------------------
print("\n--- Sample Link Texts ---")
for link in links:
    text = link.text.strip()
    if text:
        print(text)

# -------------------------------
# Keep browser open for viewing 👀
# -------------------------------
time.sleep(10)

# Close browser
driver.quit()