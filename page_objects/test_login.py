from .login import goto_website

def test_login_functionality():
    username = 'mikatsurtest'
    password = 'Github-1!'
    base_url = 'https://github.com'

    # Call the goto_website function
    goto_website(username, password, base_url)