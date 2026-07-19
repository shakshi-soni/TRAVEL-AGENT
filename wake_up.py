from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://travelagent-bqtmr6s69hxtqk8oxibuqj.streamlit.app/")
time.sleep(5)

try:
    button = driver.find_element(By.XPATH, "//button[contains(text(),'get this app back up')]")
    button.click()
    print("App was asleep — clicked wake button")
except Exception as e:
    print("App already awake (or button not found):", e)

time.sleep(10)
driver.quit()
