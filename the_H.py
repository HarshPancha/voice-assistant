from selenium import webdriver
from time import sleep
import keyboard
from pynput.keyboard import Key, Controller

class Instabot :
    def __init__(self,username,pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text() , 'Log in')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
      
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(2)

        self.driver.find_element_by_xpath("//button[contains(text() , 'Not Now')]").click()

        #self.driver.execute_script('arguments[0].scrollIntoView()')
        #self.driver.execute_script("window.scrollTo(0, 1000)") 
        self.SCROLL_PAUSE_TIME = 3

        a=0
        while a<5:
            self.driver.execute_script("window.scrollTo(0, {})".format(a*1500))
            a=a+1
            sleep(2)
        
        
class youtube:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.youtube.com/watch?v=3MHzNfoulwI")
        self.keyboard = Controller()
        self.keyboard.press(Key.space)
        self.keyboard.release(Key.space)

        sleep(16)

    

class youtube1:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.youtube.com")        

        sleep(2)

    def search(self,text):
        self.driver.find_element_by_xpath("//input[@id=\"search\"]").send_keys(text)
        self.keyboard = Controller()
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)

#youtube()

#Instabot('theproject164' , 'project')
