from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import os
import requests
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=C:/Users/Admin/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 600)
def tweet( name):
    url = "https://twitter.com/{}".format(name)
    driver.get(url)
    time.sleep(8)
    datetimelist = []
    timelength = driver.execute_script("return document.getElementsByTagName('time').length")
    for timee in range(timelength):
        dateetimee = datetime.fromisoformat(driver.execute_script(f"return document.getElementsByTagName('time')[{timee}].dateTime")[:-1])
        datetimelist.append(dateetimee)
    latesttweet = max(datetimelist)
    tweetindex = datetimelist.index(latesttweet)
    tweettext = driver.execute_script(f"return document.getElementsByClassName('css-1dbjc4n r-1loqt21 r-18u37iz r-1ny4l3l r-1udh08x r-1qhn6m8 r-i023vh r-o7ynqc r-6416eg')[{tweetindex}].children[0].children[0].children[0].children[1].children[1].children[1].children[0].children[0].textContent")
    undef = driver.execute_script(f"return typeof document.getElementsByClassName('css-1dbjc4n r-1loqt21 r-18u37iz r-1ny4l3l r-1udh08x r-1qhn6m8 r-i023vh r-o7ynqc r-6416eg')[{tweetindex}].children[0].children[0].children[0].children[1].children[1].children[1].children[1].children[0] !== 'undefined'")
    print(undef)
    if undef:
        tweetimg = driver.execute_script(f"return document.getElementsByClassName('css-1dbjc4n r-1loqt21 r-18u37iz r-1ny4l3l r-1udh08x r-1qhn6m8 r-i023vh r-o7ynqc r-6416eg')[{tweetindex}].children[0].children[0].children[0].children[1].children[1].children[1].children[1].getElementsByClassName('css-9pa8cd')[0].src")
    else:
        tweetimg = "no"
    print(tweetimg)
    twitter_url = driver.execute_script(f"return document.getElementsByClassName('css-4rbku5 css-18t94o4 css-901oao r-14j79pv r-1loqt21 r-1q142lx r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-3s2u2q r-qvutc0')[{tweetindex}].href")
    print(twitter_url)
    if os.environ.get(name+"LAST_IMAGE_ID") == str(twitter_url):
        print("Not new image to post in discord.")
    else:
        os.environ[name+"LAST_IMAGE_ID"] = str(twitter_url)
        send(twitter_url, tweetimg, tweettext)
def send(url, img, text):
    driver.get("https://web.whatsapp.com/")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '._1Jn3C')))
    time.sleep(4)
    print("yes")
    driver.find_element_by_xpath("//span[@title='Amita']").click()
    time.sleep(1)
    inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
    input_box = driver.find_element_by_xpath(inp_xpath)
    actions = ActionChains(driver)
    actions.move_to_element(input_box)
    actions.send_keys(text).perform()

    if img != "no":
        r = requests.get(img, stream = True)
        if r.status_code == 200:
            with open("tweet.jpg", 'wb') as f:
                for chunk in r:
                    f.write(chunk)
        attachment_box = driver.find_element_by_xpath(
                    '//div[@title="Attach"]')
        attachment_box.click()
        time.sleep(1)

        image_box = driver.find_element_by_xpath(
            '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        image_box.send_keys(r"C:\Users\Admin\Desktop\tweet.jpg")
        time.sleep(2)
        driver.execute_script('return document.getElementsByClassName("_165_h _2HL9j")[0].click()')
        time.sleep(2)
    else:
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '._4sWnG')))
        driver.execute_script('return document.getElementsByClassName("_4sWnG")[0].click()')

    print("SENT")

while True:
    tweet("ladygaga")
    time.sleep(40)
