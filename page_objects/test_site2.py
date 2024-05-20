from .site_2 import goto_github_search

def test_login_functionality():
    url = 'https://simonsmith.github.io/github-user-search/#/search'

    goto_github_search(url)
