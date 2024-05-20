from config.config import Config
from pages.github_search_page import GitHubSearchPage

def test_search_functionality():
    config_path = 'config/config.ini'
    config = Config(config_path)
    github_search_url = config.get_github_search_url()

    page = GitHubSearchPage(github_search_url)
    page.goto()
    page.search_user("mikatsur")
