#automation_tests\tests\test_github_search.py
import pytest
from pages.github_search_page import GitHubSearchPage

def test_search_functionality(page, config):
    github_search_url = config.get_github_search_url()
    username = config.username()
    github_search_page_obj = GitHubSearchPage(page)
    github_search_page_obj.goto(github_search_url, username)
    github_search_page_obj.assert_search_results(username)