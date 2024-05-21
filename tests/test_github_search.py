#automation_tests\tests\test_github_search.py
import pytest
from pages.github_search_page import GitHubSearchPage

def test_search_functionality(page, config):
    github_search_url = config.get_github_search_url()
    page_obj = GitHubSearchPage(page)
    page_obj.goto(github_search_url)
    # Additional test steps if needed
    page_obj.search_function