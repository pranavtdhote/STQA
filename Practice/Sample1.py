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
driver.get(r"https://www.qa-practice.com/elements/checkbox/mult_checkbox")
driver.maximize_window()

# Wait for page load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "body"))
)

# -------------------------------
# Find all checkboxes
# -------------------------------
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

checked = 0
unchecked = 0

# -------------------------------
# Count checked & unchecked
# -------------------------------
for box in checkboxes:
    if box.is_selected():
        checked += 1
    else:
        unchecked += 1

print("Total Checkboxes:", len(checkboxes))
print("Checked:", checked)
print("Unchecked:", unchecked)

time.sleep(10)

# Close browser
driver.quit()

