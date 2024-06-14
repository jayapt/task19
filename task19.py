from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class LoginPage:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()


    def quit(self):
        self.driver.quit()

    def login(self):
        username_input = self.driver.find_element(by=By.NAME, value="user-name")
        password_input = self.driver.find_element(by=By.NAME, value="password")

        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")

        self.driver.find_element(by=By.ID, value="login-button").click()
        sleep(5)

    def getTitle(self):
        return self.driver.title

    def getCurrentURL(self):
        return self.driver.current_url

        # Get the page source
    def getsourceCode(self):
        return self.driver.page_source

    def save_page_content_to_file(self, filename):
        page_content = self.getsourceCode()
        with open(filename, "w") as file:
             file.write(page_content)
        print(f"SourceCode saved to {filename}")
    #def sourceCode(self):
     #   return self.driver.page_source


url = "https://www.saucedemo.com/"

obj = LoginPage(url)
obj.boot()
obj.login()
current_url = obj.getCurrentURL()
print("Current URL of the webpage:", current_url)
title = obj.getTitle()
print("Title of the webpage:", title)
# Save the entire content of the webpage to a text file
obj.save_page_content_to_file("webpage_task_11.txt")
obj.quit()
