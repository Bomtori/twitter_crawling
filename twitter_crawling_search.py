from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#검색어 입력
search_what = input("검색어를 입력하세요 : ")
inputID = input("아이디를 입력하세요 : ")
inputPW = input("비밀번호를 입력하세요 : ")

driver = webdriver.Chrome()
driver.get("https://twitter.com/i/flow/login?redirect_after_login=%2F")

driver.implicitly_wait(20)

###로그인 기능
#ID 입력
ID_box = driver.find_element(By.CSS_SELECTOR, 'input.r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu')
ID_box.send_keys(inputID)
ID_box.send_keys(Keys.RETURN)
print('input ID')
driver.implicitly_wait(5)

#PW 입력
PW_box = driver.find_element(By.CSS_SELECTOR, 'input.r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu')
PW_box.send_keys(inputPW)
PW_box.send_keys(Keys.RETURN)
print('input PW')
driver.implicitly_wait(20)

###검색어 기능

#검색 버튼 클릭
search_button = driver.find_element(By.CSS_SELECTOR, 'a[data-testid="AppTabBar_Explore_Link"]').click()
print('explore button click')
driver.implicitly_wait(20)

#검색어란에 검색어 입력
search_box = driver.find_element(By.CSS_SELECTOR, 'input.r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-xyw6el.r-y0fyvk.r-1dz5y72.r-fdjqy7.r-13qz1uu')
search_box.send_keys(search_what)
search_box.send_keys(Keys.RETURN)
print('input search')
driver.implicitly_wait(20)

#검색 후 사용자의 ID를 가져옴
print("start")
print("-" * 50)

user_name_selector = 'div[data-testid="User-Name"]'
user_sub_selector = 'div[data-testid="tweetText"]'

# 스크롤을 반복하며 정보를 가져옵니다.
scroll_pause_time = 1  # 스크롤링 간 일시 정지할 시간 (초)
scroll_count = 5  # 스크롤 다운할 횟수

for i in range(scroll_count):
    # 현재 화면의 높이를 저장합니다.
    last_height = driver.execute_script("return document.body.scrollHeight")

    # 정보를 가져옵니다.
    user_name_elements = driver.find_elements(By.CSS_SELECTOR, user_name_selector)
    user_sub_elements = driver.find_elements(By.CSS_SELECTOR, user_sub_selector)

    for name_element, sub_element in zip(user_name_elements, user_sub_elements):
        user_name = name_element.find_element(By.CSS_SELECTOR, 'span.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0')
        user_link = name_element.find_element(By.CSS_SELECTOR, 'a').get_attribute("href")
        # datetime = name_element.find_element(By.CSS_SELECTOR, 'span.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0')

        print("이름:", user_name.text)
        print("내용:", sub_element.text)
        # print("날짜:", datetime.text)
        print("링크:", user_link)
        print("-" * 50)

    # 페이지를 스크롤 다운합니다.
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 페이지 로딩을 기다립니다.
    time.sleep(scroll_pause_time)

    # 스크롤 다운 후의 화면 높이를 가져옵니다.
    new_height = driver.execute_script("return document.body.scrollHeight")

    # 만약 스크롤이 더 이상 되지 않으면 반복을 종료합니다.
    if new_height == last_height:
        break

    # 다음 스크롤링을 위해 last_height를 업데이트합니다.
    last_height = new_height

# 웹 드라이버를 종료합니다.
driver.quit()
print('finish')