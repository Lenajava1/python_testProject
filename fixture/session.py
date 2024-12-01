from selenium.webdriver.common.by import By

class SessionHelper:

     def __init__(self, app):
         self.app = app

     def login(self, username, password):
         wd = self.app.wd
         self.app.open_home_page()
         wd.find_element(By.NAME, "username").click()
         wd.find_element(By.NAME, "username").clear()
         wd.find_element(By.NAME, "username").send_keys(username)
         wd.find_element(By.XPATH, '//input[@type="submit"]').click()
         wd.find_element(By.NAME, "password").click()
         wd.find_element(By.NAME, "password").clear()
         wd.find_element(By.NAME, "password").send_keys(password)
         wd.find_element(By.XPATH, '//input[@type="submit"]').click()

     def logout(self):
         wd = self.app.wd
         wd.find_element(By.XPATH, "//a[@class='dropdown-toggle']//span[1]").click()
         wd.find_element(By.XPATH, "//a[@href='/mantisbt-2.27.0/logout_page.php']").click()


     def ensure_logout(self):
         wd = self.app.wd
         if self.is_logged_in():
            self.logout()

     def is_logged_in(self):
         wd = self.app.wd
         return len(wd.find_elements(By.NAME, "logout")) > 0

     def get_user_name(self):
         wd = self.app.wd
         return wd.find_element(By.CSS_SELECTOR, "div#breadcrumbs>ul>li>span").text

     def is_logged_in_as(self, username):
         return self.get_user_name() == username

     def ensure_login(self, username, password):
         wd = self.app.wd
         if self.is_logged_in():
             if self.is_logged_in_as(username):
                 return
             else:
                 self.logout()
         self.login(username, password)



