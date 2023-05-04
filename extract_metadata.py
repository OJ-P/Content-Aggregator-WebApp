from newspaper import Article

def summarise_article(url):
    
    article = Article(url)
    article.download()
    article.parse()
    article.download('punkt')
    article.nlp()
    
    author = str(article.authors)
    publish_date_raw = article.publish_date
    publish_date_formatted = str(publish_date_raw.strftime("%d%m%Y"))
    
