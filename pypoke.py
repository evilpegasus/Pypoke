from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from time import sleep
from secrets import username, password

option = Options()
# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2 
})

class pypoke:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome(chrome_options = option)
        self.driver.get("https://www.facebook.com/pokes/")
        print("Going to Facebook")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"email\"]")\
            .send_keys(username)
        sleep(1)
        self.driver.find_element_by_xpath("//input[@name=\"pass\"]")\
            .send_keys(password)
        sleep(1)
        self.driver.find_element_by_xpath("//button[@name=\"login\"]").click()
        print("Logging in")
        sleep(4)


        while True:
            self.driver.find_element_by_link_text("Poke Back").click
                # .click
            print("Clicked Poke Back button")
            # try:
            #     self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[3]/div/div/div/div[1]/div/a[1]")\
            #         .click
            #     print("Clicked Poke Back button")
            #     sleep(4)
            # except NoSuchElementException:
            #     print("Poke Back button not found")
            sleep(4)
        

# poke = pypoke(input("Username: "), input("Password: "))
# print(username + " " + password)
pypoke(username(), password())