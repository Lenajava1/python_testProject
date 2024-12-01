from selenium.webdriver.common.by import By
from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_tab(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//a[@href='/mantisbt-2.27.0/manage_overview_page.php']").click()
        wd.find_element(By.LINK_TEXT, "Projects").click()

    def fill_project_form(self,project):
        wd = self.app.wd
        wd.find_element(By.ID, "project-name").click()
        wd.find_element(By.ID, "project-name").clear()
        wd.find_element(By.ID, "project-name").send_keys(project.name)
        wd.find_element(By.ID, "project-description").click()
        wd.find_element(By.ID, "project-description").clear()
        wd.find_element(By.ID, "project-description").send_keys(project.description)

    def create_new_project(self,project):
        wd = self.app.wd
        self.open_project_tab()
        wd.find_element(By.XPATH, '(//button[@type="submit"])[1]').click()
        self.fill_project_form(project)
        wd.find_element(By.XPATH, '//input[@type="submit"]').click()

    def count(self):
        wd = self.app.wd
        self.open_project_tab()
        return len(wd.find_elements(By.XPATH, "//td/a[@href]"))

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_tab()
            self.project_cache = []
            for element in wd.find_elements(By.TAG_NAME, "td"):
                cells = element.find_elements(By.TAG_NAME, "td")
                name = cells[1].text
                self.project_cache.append(Project(name=name))
        return list(self.project_cache)







