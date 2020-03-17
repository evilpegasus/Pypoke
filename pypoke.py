from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from secrets import username, password
from getpass import getpass

option = Options()
# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2 
})

class pypoke:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome(options = option)
        self.driver.get("https://www.facebook.com/pokes/")
        print("Going to Facebook")
        sleep(1)
        self.driver.find_element_by_xpath("//input[@name=\"email\"]").clear()
        self.driver.find_element_by_xpath("//input[@name=\"email\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"pass\"]").clear()
        self.driver.find_element_by_xpath("//input[@name=\"pass\"]").send_keys(password)
        sleep(1)
        self.driver.find_element_by_xpath("//button[@name=\"login\"]").click()
        print("Logging in")
        sleep(1)

        #incase of incorrect username/password
        while (self.check_exists_by_xpath(self, "//input[@name=\"email\"]") or self.check_exists_by_xpath(self, "//input[@name=\"pass\"]")):
            print("Failed to login, please reenter email and password")
            username = input("Username: ")
            password = getpass("Password (input is hidden): ")
            self.driver.find_element_by_xpath("//input[@name=\"email\"]").clear()
            self.driver.find_element_by_xpath("//input[@name=\"email\"]").send_keys(username)
            self.driver.find_element_by_xpath("//input[@name=\"pass\"]").clear()
            self.driver.find_element_by_xpath("//input[@name=\"pass\"]").send_keys(password)
            sleep(1)
            self.driver.find_element_by_xpath("//button[@name=\"login\"]").click()
            print("Logging in")
            sleep(1)

        #poke loop
        count = 0
        while True:
            try:
                self.driver.find_element_by_link_text("Poke Back").send_keys(Keys.RETURN)
                count += 1
                print("Clicked Poke Back button " + str(count) + " times")
            except NoSuchElementException:
                print("Poke Back button not found")
            sleep(4)
    
    @classmethod
    def check_exists_by_xpath(cls, self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

poke = pypoke(input("Username: "), getpass("Password (input is hidden): "))
# pypoke(username(), password())