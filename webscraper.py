import requests
from bs4 import BeautifulSoup
import re


class NytimesArticles:

    def __init__(self, page_to_scrape):
        self.page_to_scrape = page_to_scrape  

    def get_content(self, url):
        request = requests.get(url)
        soup = BeautifulSoup(request.text, 'html.parser')
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

    def extract_link_index(self, content_str, current_year):
        start_index = []
        end_index = []
        for i in range(len(content_str)):
            if content_str.startswith(f"https://www.nytimes.com/{current_year}", i):
                start_index.append(i)
            if content_str.startswith("html", i):
                end_index.append(i + 4)
        return start_index, end_index

    def extract_url(self, link_indexs, content_string):
        url_list = []
        for i in range(len(link_indexs[0])):
            url_list.append(content_string[link_indexs[0][i]:link_indexs[1][i]])
        return url_list

    def scrape_page(self):
        content_string = self.get_content(self.page_to_scrape)
        link_indexs = self.extract_link_index(content_string, 2023)
        aricle_urls = self.extract_url(link_indexs, content_string)
        return aricle_urls

class IndependentArticles:

    def __init__(self, page_to_scrape, re_pattern):
        self.page_to_scrape = page_to_scrape
        self.re_pattern = re_pattern

    def get_content(self, url):
        request = requests.get(url)
        soup = BeautifulSoup(request.text, 'html.parser')
        containers = soup.find_all("a", {"class": "title"})
        content_list = re.findall(self.re_pattern, str(containers))
        return content_list

    def extract_url(self, content_list):
        url_list = []
        for link in content_list:
            link = link[6:-2]
            link = "https://www.independent.co.uk" + link
            url_list.append(link)
        return url_list

    def scrape_page(self):
        content_list = self.get_content(self.page_to_scrape)
        article_urls = self.extract_url(content_list)
        return article_urls


nytimes_tech_articles = NytimesArticles("https://www.nytimes.com/section/technology")
nytimes_science_articles = NytimesArticles("https://www.nytimes.com/section/science")
nytimes_food_articles = NytimesArticles("https://www.nytimes.com/section/food")
independent_tech_articles = IndependentArticles("https://www.independent.co.uk/tech", re.compile(r'href="\/tech\/.*?\.html">'))
independent_science_articles = IndependentArticles("https://www.independent.co.uk/news/science", re.compile(r'href="\/news\/science\/.*?\.html">'))
independent_food_articles = IndependentArticles("https://www.independent.co.uk/life-style/food-and-drink", re.compile(r'href="\/life-style\/food-and-drink\/.*?\.html">'))

#print(independent_food_articles.scrape_page())