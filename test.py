import requests
from bs4 import BeautifulSoup

URL = "https://www.facebook.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="gallery-content")

print(soup)

search_elements = results.find_all("h1")

# for search_element in search_elements:
    # title_container = search_element.find(class_="post-title")
    # title_bersih = title_container.find('a')
print(search_elements.text)