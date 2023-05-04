from textblob import TextBlob

def extract_sentiment(news_story):
    
    # split article into sentences and analyse sentiment for each sentence
    news = TextBlob(news_story)
    article_sentiments = []
    for sentence in news.sentences:
        sentiment = sentence.sentiment
        for metric in sentiment:
            article_sentiments.append(metric)
    
    # polarity always the 2nd data entry (even number indicie) else it is subjectivity data
    polarity = []
    subjectivity = []
    for index in range(len(article_sentiments)):
        if index % 2 == 0:
            polarity.append(article_sentiments[index])
        else:
            subjectivity.append(article_sentiments[index])

    polarity_average = calc_average(polarity)
    subjectivity_average = calc_average(subjectivity)

    final_polarity = categorise_sentiment(polarity_average, "polarity")
    final_subjectivity = categorise_sentiment(subjectivity_average, "subjectivity")
    
def calc_average(list):
    return sum(list) / len(list)

def categorise_sentiment(average_sentiment, type):

    sentiment_category = ""

    if type == "polarity":
        if average_sentiment > 0.75:
            sentiment_category = "Extremely Positive"
        if average_sentiment > 0.5:
            sentiment_category = "Significantly Positive"
        if average_sentiment > 0.3:
            sentiment_category = "Fairly Positive"
        if average_sentiment > 0.1:
            sentiment_category = "Slightly Positive"
        if average_sentiment < -0.1:
            sentiment_category = "Slightly Negative"
        if average_sentiment < -0.3:
            sentiment_category = "Fairly Negative"
        if average_sentiment < -0.5:
            sentiment_category = "Significantly Negative"
        if average_sentiment < -0.75:
            sentiment_category = "Extremely Negative"
    elif type == "subjectivity":
        if average_sentiment > 0.75:
            sentiment_category = "Extremely Subjective"
        elif average_sentiment > 0.5:
            sentiment_category = "Fairly Subjective"
        elif average_sentiment > 0.3:
            sentiment_category = "Extremely Objective"
        elif average_sentiment > 0.1:
            sentiment_category = "Fairly Objective"
    return sentiment_category


