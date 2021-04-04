# python -m pip install <package> to install
import requests
from bs4 import BeautifulSoup as bs

# collect github user
github_user = input('Input GitHub User: ')
# page i'm sending a request to
url = 'https://github.com/, {}'.format(github_user)