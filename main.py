from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tkinter import messagebox
import time

try:
    servise = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=servise)
    driver.maximize_window()
    driver.get("https://clickspeedtest.com/")
    WebDriverWait(driver, 2).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "rbutton")))
    click_btn = driver.find_element(By.CLASS_NAME, "rbutton")
    for i in range(70):
        click_btn.click()
    time.sleep(20)
    driver.quit()
except:
    messagebox.showerror(title="Error", message="Connection Problem")