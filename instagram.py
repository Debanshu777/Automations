from selenium import webdriver
import time


class Instabot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.username = 'debanshu.datta'
        self.driver.get("https://www.instagram.com")
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(
            'debanshu.datta')
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(
            'Abcd')
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()

    def get_unfollowers(self):
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a').click()
        time.sleep(3)
        sugs = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click()
        self.driver.execute_script('arguments[0].scrollIntoView(true);', sugs)
        time.sleep(2)
        scroll_view = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(1)
            ht = self.driver.execute_script('''
            arguments[0].scrollTo(0,arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            ''', scroll_view)


my_bot = Instabot()
my_bot.get_unfollowers()
