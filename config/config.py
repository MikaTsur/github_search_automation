import configparser
import os

# an easier way to do this is to use a combination of yaml with python-box
# you can replace this entire class by two lines
# dictionary = yaml.load(open('config.yaml'))
# config = box.Box(dictionary)
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
