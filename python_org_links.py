import requests
from bs4 import BeautifulSoup
import re
while True:
    keyword = input("Enter the keyword you want to search for: ")
    url = "https://www.google.com/search?q=" + keyword
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a')

    for link in links:
        href = link.get('href')
        if href.startswith("/url?q="):
            href = re.search(r'(?<=/url\?q=).*?(?=&)', href).group(0)
            print(href)
    