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
    return content_string
    

def extract_link_index(content_str, current_year):
    start_index = []
    end_index = []
    for i in range(len(content_str)):
        if content_str.startswith(f"https://www.nytimes.com/{current_year}", i):
            start_index.append(i)
        if content_str.startswith("html", i):
            end_index.append(i + 4)
    return start_index, end_index


def extract_url(link_indexs, cotent_string):
    url_list = []
    for i in range(len(link_indexs[0])):
        url_list.append(content_string[link_indexs[0][i]:link_indexs[1][i]])
    return url_list

content_string = get_content("https://www.nytimes.com/section/technology")
link_indexs = extract_link_index(content_string, 2023)
aricle_urls = extract_url(link_indexs, content_string)

