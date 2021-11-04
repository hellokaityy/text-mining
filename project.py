from newspaper import Article
from nltk.sentiment.vader import SentimentIntensityAnalyzer


url1 = 'https://www.cbsnews.com/live-updates/trump-us-capitol-secured-dc-protest/'
articleCBS = Article(url1)
url2 = 'https://www.foxnews.com/politics/how-wednesdays-capitol-riot-come-to-fruition'
articleFox = Article(url2)
articleCBS.download()
articleCBS.parse()



sentence = 'Software Design is my favorite class because learning Python is so cool!'
score = SentimentIntensityAnalyzer().polarity_scores(sentence)
print(score)


