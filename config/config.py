#config.py
import yaml
from box import Box
import os

class Config:
    def __init__(self, config_path):
        with open(config_path, 'r') as file:
            self.config = Box(yaml.safe_load(file))

    def get_github_search_url(self):
        try:
            return self.config.github.github_search_url
        except KeyError as e:
            print(f"Configuration key not found: {e}")
            exit(1)

    def username(self):
        try:
            return self.config.github.username
        except KeyError as e:
            print(f"Configuration key not found: {e}")
            exit(1)

# Usage example:
if __name__ == "__main__":
    config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
    config = Config(config_path)
    print(config.get_github_search_url())
