import requests
from bs4 import BeautifulSoup

def scrape(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = [tag.text for tag in soup.find_all('h2')]
    return titles

if __name__ == "__main__":
    url = "https://news.ycombinator.com/"
    for title in scrape(url):
        print("-", title)