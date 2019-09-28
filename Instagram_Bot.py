from selenium import webdriver
import requests, random
import time
import os
from os import path, listdir, unlink
import shutil
from bs4 import BeautifulSoup
import pyautogui as auto
from urllib.request import urlretrieve
from multiprocessing import Process


class Chrome:
    url = 'https://www.brainyquote.com/quote_of_the_day'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    img = soup.find('img')['alt']
    quote = img.split('-')[0]

    def __init__(self):

        url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
        chrome = webdriver.Chrome('c:\\Users\\ABC\\Desktop\\chromedriver.exe')
        chrome.get(url)

        def email():
            try:
                user = chrome.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
                user.send_keys(' EMAIL ADDRESS')
            except Exception:
                time.sleep(3)
                email()

        email()

        def password():
            try:
                password = chrome.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
                password.send_keys(' PASSWORD ')
            except Exception:
                time.sleep(3)
                password()

        password()

        # log in click
        time.sleep(1)
        chrome.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button').click()

        Process(target=self.image).start()
        self.auto(chrome)

    @staticmethod
    def img_delete():
        folder = 'C:/Users/ABC/Documents/Instagram_photos'
        for i in listdir(folder):
            file = path.join(folder, i)
            try:
                if path.isfile(file):
                    unlink(file)
                else:
                    shutil.rmtree(file)
            except Exception:
                pass

    @staticmethod
    def image():
        api = f'https://api.unsplash.com/photos/search?query=programming-or-hacking&resolution=1500&orientation=landscape&client_id=8c8b90902c54cea3f2f2cab40bdb8f20312086c3342fe83428f930c72e6e2219&page={random.randint(1,10)}&w=1500&dpi=2'  # This is pixel size 1500, 1080,400,200
        res = requests.get(api).json()
        if 'error' in res: print(res['error'])

        image_list = []
        for i in range(9):
            url = res[i]['links']['download']

            if os.path.exists('C:/Users/ABC/Documents/Instagram_photos'): os.chdir('C:/Users/ABC/Documents/Instagram_photos')
            else:
                os.mkdir('C:/Users/ABC/Documents/Instagram_photos')
                os.chdir('C:/Users/ABC/Documents/Instagram_photos')

            name_of_image = str(res[i]['alt_description'])
            img_name = '_'.join(name_of_image[:40].split(' '))
            image_list.append([url, img_name+'.jpg'])

        img_select = random.randint(0, 9)
        # download one image
        urlretrieve(image_list[img_select][0], image_list[img_select][1])



    def auto(self, chrome):
        # this is click on instagram side page
        auto.moveTo(x=332, y=350, duration=.2)
        auto.click()
        time.sleep(5)

        # press these keys to get 'Dev tool'
        auto.hotkey('shift','ctrl', 'j')
        time.sleep(3)

        # It's moving to click mobile view
        auto.moveTo(x=541, y=146, duration=.2)
        time.sleep(1)
        auto.click()

        # waiting until page not load
        def until_page_not_load():
            try:
                chrome.find_element_by_class_name('_1SP8R')
            except Exception:
                time.sleep(3)
                until_page_not_load()
        until_page_not_load()

        auto.press('f5')
        time.sleep(1)

        # wating until page not load
        def until_page_not_load():
            try:
                chrome.find_element_by_class_name('_1SP8R')
            except Exception:
                time.sleep(3)
                until_page_not_load()
        until_page_not_load()


        # press keys to hide 'Dev tool'
        auto.hotkey('shift', 'ctrl', 'j')
        time.sleep(3)


        # close notification
        def close_notification():
            try:
                time.sleep(3)
                chrome.find_element_by_class_name('HoLwm').click()
            except Exception:
                print('we didn\'t get notification')

        close_notification()

        # click to open file manger to add image
        def icon_image_uploader():
            try:
                chrome.find_element_by_xpath('//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[3]/span').click()
            except Exception:
                time.sleep(3)
                icon_image_uploader()

        icon_image_uploader()

        # selection of folder and after image
        # folder = Documents
        time.sleep(2)
        auto.click(x=140, y=255, duration=.2)
        time.sleep(2)

        # folder = Instagram photos
        auto.click(x=491, y=190, duration=.2)
        auto.click(x=491, y=190, duration=.2)
        time.sleep(1)

        # change extension of images
        auto.click(x=663, y=601, duration=.2)
        time.sleep(1)
        auto.click(x=663, y=640, duration=.2)

        # select first image inside Instagram photos folder
        auto.click(x=237, y=170, duration=.2)
        time.sleep(1)
        # click to open (windows button)
        auto.click(x=636, y=632, duration=.2)
        time.sleep(2)

        # scroll down to zoom out image
        def scrool_down():
            [auto.press('down') for _ in range(14)]

        scrool_down()

        # zoom out image size
        def zoom_out_image():
            try:
                chrome.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/div[2]/div/div/div/button[1]/span').click()
            except Exception:
                time.sleep(1)
                zoom_out_image()

        zoom_out_image()


        # click button to next
        def click_to_next_button():
            try:
                chrome.find_element_by_xpath('//*[@id="react-root"]/section/div[1]/header/div/div[2]/button').click()
            except Exception:
                time.sleep(2)
                click_to_next_button()

        click_to_next_button()


        # write caption of image
        def image_caption():
            try:
                text_tag = chrome.find_element_by_tag_name('textarea')
                text_tag.click()

                text_tag.send_keys(self.quote + '\n\n\n\n\n\n\n\n\nFollow @rohit_dalal_0 for Coding, Programming fun and Information.\n\n\n\n\n#programming #coding #programmer #programminglife# coder #javascript #fullstackdeveloper #codingmemesw @rohit #programmers #cplusplus #programmingisfun #developer #coders #neuralnetworks #html #webdeveloper #programmerslife #css #python #compiler #python3 #backenddeveloper #androiddeveloper #webdevelopment #hacking #cprogramming #programmingmemes #deeplearning #softwaredeveloper')
            except Exception:
                time.sleep(2)
                image_caption()

        image_caption()

        # final click to share button
        def share_image():
            try:
                chrome.find_element_by_xpath('//*[@id="react-root"]/section/div[1]/header/div/div[2]/button').click()
            except Exception:
                time.sleep(2)
                share_image()

        share_image()

        # after publish image will be delete
        Process(target=self.img_delete).start()
        time.sleep(5)

        chrome.close()





if __name__ == "__main__":
    start = Chrome()
