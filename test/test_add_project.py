from model import project
from model.project import Project


def test_add_project(app, project):
    #if app.project.count() == 0:
    app.project.create_new_project(project)
    old_projects = app.project.get_project_list()
    app.project.create_new_project(project)
    assert len(old_projects) + 1 == app.project.count()
