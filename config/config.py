import configparser
import os

class Config:
    def __init__(self, config_path):
        self.config = configparser.ConfigParser()
        self.config.read(config_path)

    def get_github_search_url(self):
        try:
            return self.config['github']['github_search_url']
        except KeyError as e:
            print(f"Configuration key not found: {e}")
            exit(1)
