# -*-coding:utf-8-*-
from selenium import webdriver
import json
import time

#
# driver = webdriver.Chrome()
# driver.get("https://twitter.com/login")
# time.sleep(60)
# cookies = driver.get_cookies()
# with open("qrsncookies.txt", "w") as fp:
#     json.dump(cookies, fp)
# # https://twitter.com/login

def read_cookies():
    driver = webdriver.Chrome()
    # option = webdriver.ChromeOptions()
    # option.add_argument("headless")
    # driver = webdriver.Chrome(chrome_options=option)
    driver.get("https://twitter.com/login")
    with open("cheshicookies.txt", "r") as fp:
        cookies = json.load(fp)
        for cookie in cookies:
            driver.add_cookie(cookie)

    driver.get("https://twitter.com/login")
    return driver


def publish(list):
    driver = read_cookies()
    # time.sleep(5)
    print(list)
    driver.find_element_by_xpath('//*[@id="tweet-box-home-timeline"]').click()
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="tweet-box-home-timeline"]').send_keys(list[1])
    print(list[1])
    time.sleep(20)
    lenth = len(list)
    for lis in list[2:lenth]:
        lis = lis.strip()
        driver.find_element_by_xpath('//*[@id="timeline"]/div[2]/div/form/div[3]/div[1]/span[1]/div/div/label/input').send_keys("D:\dev\weiboimg\\"+lis)
        print(lis)
        time.sleep(1)

    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="timeline"]/div[2]/div/form/div[3]/div[2]/button/span[1]').click()
    time.sleep(10)
    driver.quit()
# time.sleep(3)

#
driver = read_cookies()
# time.sleep(5)
driver.find_element_by_xpath('//*[@id="tweet-box-home-timeline"]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="tweet-box-home-timeline"]').send_keys("hello luxun")
time.sleep(10)
driver.find_element_by_xpath(
    '//*[@id="timeline"]/div[2]/div/form/div[3]/div[1]/span[1]/div/div/label/input').send_keys(
    "D:\work\weiboimg\\4271878254492031.mp4")

time.sleep(1)
driver.find_element_by_xpath('//*[@id="timeline"]/div[2]/div/form/div[3]/div[2]/button/span[1]').click()


