

def test_login(app):
    app.session.login("administrator", "Password1")
    assert app.session.is_logged_in_as("administrator")
