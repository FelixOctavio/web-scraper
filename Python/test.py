import requests
from bs4 import BeautifulSoup

anime = input("Masukkan Anime yang ingin dicari: ")

URL = "https://anidl.org/?s=" + str(anime)
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="posts-container")

search_elements = results.find_all("div", class_="post-details")

print("\nAniDL\n")
for search_element in search_elements:
    title_container = search_element.find(class_="post-title")
    title_bersih = title_container.find('a')
    print(title_bersih.text)
    
URL = "https://animeout.xyz/?s=" + str(anime)
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(class="row responsive-cols kleo-masonry per-row-4")

search_elements = results.find_all("div", class_="post-details")

print("\nAniDL\n")
for search_element in search_elements:
    title_container = search_element.find(class_="post-title")
    title_bersih = title_container.find('a')
    print(title_bersih.text)