#automation_tests\tests\test_github_search.py
import pytest
from pages.github_search_page import GitHubSearchPage
# the `from module import name` pattern is popular,
# but it's bad, see [Import Modules Not Names](https://github.com/PracticeFoxyCode/practice#import-modules-not-names-namespaces-and-import-statements)

def test_search_functionality(page, config):
    github_search_url = config.get_github_search_url()

    page_obj = GitHubSearchPage(page)
    page_obj.goto(github_search_url)
# the name page_obj violates two rules
# it's not just any page, it's the github search page
# so it should be called github_search_page
# 
# note, github_search_page and NOT github_search_page_obj
# the suffix _obj tells us nothing - everything in python is an object

    # Additional test steps if needed
