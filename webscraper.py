import requests
from bs4 import BeautifulSoup
import io


def get_content(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    with open('outputfile.txt', 'w', encoding="utf-8") as f:
        f.write(soup.prettify())
    containers = soup.find_all("script", {"type": "application/ld+json"})
    article_list = []
    for container in containers:
        for dictionary in container:
            article_list.append(dictionary)
    article_list[0:2] = [''.join(article_list[0:2])]
    content_string = article_list[0]
    article_index = content_string.index("itemListElement")
    content_string = content_string[article_index + 18:]
    

get_content("https://www.nytimes.com/section/technology")

