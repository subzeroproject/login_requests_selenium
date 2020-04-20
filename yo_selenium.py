
from selenium import webdriver

class LoginLit():
    #mở browser với chromedriver
    driver = webdriver.Chrome('C:\Python38\Scripts\chromedriver.exe')
    def login(self):
        #điều hướng browser đến url
        self.driver.get('https://cm.litextension.com/login')

        #tìm xpath ô đăng nhập và auto nhập
        username = "test1@test.com"
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        password = "aA123456"
        password_in = self.driver.find_element_by_xpath('//*[@id="password"]')
        password_in.send_keys(password)

        #tìm xpath button login và click
        submit = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/div[1]/form/div[5]/div/button')
        submit.click()

        user = self.driver.find_element_by_xpath('//*[@id="navbarDropdown2"]')
        user.click()

        user = self.driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[4]/ul/li[1]/a')
        user.click()

        #in tên user vừa đăng nhập ra python shell
        name = self.driver.find_element_by_xpath('//*[@id="profile"]/div[1]/div[1]/div/h3')
        id = name.get_attribute("innerHTML")
        print(id)
        
bot = LoginLit()
bot.login()
