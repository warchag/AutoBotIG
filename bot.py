from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import  urllib.request
import os
class Instargram:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.BaseUrl = "https://www.instagram.com/"
    def Login(self):
        self.driver.get(f"{self.BaseUrl}accounts/login/")
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(self.username)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(self.password + Keys.ENTER)
        time.sleep(3)
        self.driver.find_elements_by_xpath("//button[contains(text(),'Not Now')]")[0].click()
    def Nav_user(self,user):
        self.driver.get(f"{self.BaseUrl}{user}")
        time.sleep(2)
    def Follow_user(self,user):
        self.Nav_user(user)
        self.driver.find_elements_by_xpath("//button[contains(text(),'Follow')]")[0].click()
    def Unfollow_user(self,user):
        self.Nav_user(user)
        self.driver.find_elements_by_xpath("//button[contains(text(),'Following')]")[0].click()
        time.sleep(1)
        self.driver.find_elements_by_xpath("//button[contains(text(),'Unfollow')]")[0].click()

    def Search_Tag(self,hashtag):
        self.driver.get(f"{self.BaseUrl}explore/tags/{hashtag}")
        time.sleep(2)

    def Like_photo(self,count):
        self.driver.find_element_by_class_name('eLAPa').click()
        i = 1
        img_srcs = []
        while  i <= count:
            time.sleep(1)
            #self.driver.find_element_by_class_name('wpO6b').click()
            img_srcs.extend([img.get_attribute('src') for img in self.driver.find_elements_by_class_name('FFVAD')]) # scrape srcs
            img_srcs = list(set(img_srcs))
            time.sleep(0.5)
            self.driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            i+=1
            print("===== start to Download_photo======")
        self.Download_photo(img_srcs)
    def Download_photo(self,photolist):
        i = 1
        for urlpic in photolist:
            i += 1
            folder_path = './{}'.format("folder")
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
            img_filename = 'image_{}.jpg'.format(i)
            urllib.request.urlretrieve(urlpic, '{}/{}'.format("folder",img_filename))
            print(f"Download_photo = {img_filename}")

hashtags = input("=== input your tag ===")
downloadcount = int(input("=== input your downloadcount ==="))
MYBOT = Instargram("warchag01","Billkyz131")
MYBOT.Login()
MYBOT.Search_Tag(hashtags)
MYBOT.Like_photo(downloadcount)
