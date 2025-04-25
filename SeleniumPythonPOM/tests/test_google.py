from selenium import webdriver
from selenium.webdriver.common.by import By

def test_google_search():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Azure DevOps Selenium")
    search_box.submit()
    assert "Azure DevOps Selenium" in driver.page_source
    driver.quit()
