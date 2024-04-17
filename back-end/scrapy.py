import requests_tor
from bs4 import BeautifulSoup
from io import StringIO
import json


class GitHubScraper:
    def __init__(self):
        self.github_api_token = 'ghp_GB5NPbxq5CNUrkFBd@RVUbSrdxLpZ02KSRtn'
        self.urls = []

    def search_github(self, keyword):
        api = "https://api.github.com/search/repositories?q=" + keyword
        headers = {"Accept": "application/vnd.github.v3+json"}
        leak_response = requests.get(api, headers=headers)
        if leak_response.status_code == 200:
            data = json.loads(leak_response.text)
            for item in data.get("items", []):
                html_url = item.get("html_url")
                if html_url:
                    self.urls.append(html_url)

    def url_transformer(self):
        api_urls = []
        for url in self.urls:
            api_urls.append(f'https://api.github.com/repos/{url[19:]}/contents')
        for api_url in api_urls:
            print(api_url)

    def scrape(self, link, keyword):
        response = requests.get(link)
        if response.status_code == 200:
            data = response.json()
            for item in data:
                if item['type'] == 'file':
                    file_content_response = requests.get(item['download_url'])
                    if file_content_response.status_code == 200:
                        html_content = file_content_response.text
                        soup = BeautifulSoup(StringIO(html_content), 'html.parser')
                        if keyword in html_content:
                            print(f"Keyword '{keyword}' found in: {item['html_url']}")
                        else:
                            print("Nothing to be found in here")
                elif item['type'] == 'dir':
                    self.scrape(item['url'], keyword)


if _name_ == "_main_":
    scraper = GitHubScraper()
    keyword = input("Enter topic to scrap: ")
    scraper.search_github(keyword)
    scraper.url_transformer()
    keywords = input("Enter word or multiple keywords: ").split()
    for link in scraper.urls:
        for word in keywords:
            scraper.scrape(link, word) 
