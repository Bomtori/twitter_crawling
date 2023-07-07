from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
#드라이버 초기화
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#URL 얻기
driver.get("https://twitter.com/login")