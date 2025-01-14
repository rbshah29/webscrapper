import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import unquote

def google_search():
    while True:
        keyword = input("Enter the keyword you want to search for (or 'quit' to exit): ")
        if keyword.lower() == 'quit':
            break
            
        url = "https://www.google.com/search?q=" + keyword
        
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            

            links = soup.find_all('a')
            
            found_results = False
            for link in links:
                href = link.get('href')
                if href and href.startswith("/url?q="):

                    actual_url = re.search(r'(?<=/url\?q=).*?(?=&)', href)
                    if actual_url:
                        decoded_url = unquote(actual_url.group(0))
                        print(decoded_url)
                        found_results = True
            
            if not found_results:
                print("No results found for this search.")
                
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    google_search()
