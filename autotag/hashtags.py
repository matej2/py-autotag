from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.common.by import By
from autotag.settings import (
    page_url,
    upload_input,
    hashtags,
)


def get_hashtags(image_dir):
    driver = webdriver.Firefox(executable_path="/home/user/Drivers/geckodriver")
    wait = WebDriverWait(driver, 50)
    suggested_hashtags = ""
    driver.get(page_url)

    # Load webpage
    upload_element = driver.find_element_by_id(upload_input)
    upload_element.send_keys(image_dir)
    print("Web page loaded")

    # Hashtags
    wait.until(visibility_of_element_located((By.CSS_SELECTOR, hashtags)))
    hashtag_list =driver.find_elements_by_css_selector(hashtags)

    # Make serializible

    for hashtag in hashtag_list:
        suggested_hashtags += hashtag.text.replace("\u00d7", "")



    driver.close()
    driver.quit()

    return suggested_hashtags
