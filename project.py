from newspaper import Article


url1 = 'https://www.cbsnews.com/live-updates/trump-us-capitol-secured-dc-protest/'
articleCBS = Article(url1)
url2 = 'https://www.foxnews.com/politics/how-wednesdays-capitol-riot-come-to-fruition'
articleFox = Article(url2)
articleCBS.download()
articleCBS.parse()


# # Save data to a file (will be part of your data fetching script)

# with open('dickens_texts.pickle','w') as f:
#     pickle.dump(charles_dickens_texts,f)


# # Load data from a file (will be part of your data processing script)
# with open('dickens_texts.pickle','r') as input_file:
#     reloaded_copy_of_texts = pickle.load(input_file)


# Here is an example of doing [sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis):
# ```
# from nltk.sentiment.vader import SentimentIntensityAnalyzer

# sentence = 'Software Design is my favorite class because learning Python is so cool!'
# score = SentimentIntensityAnalyzer().polarity_scores(sentence)
# print(score)
# ```
# This program will print out:
# ```
# {'neg': 0.0, 'neu': 0.614, 'pos': 0.386, 'compound': 0.7417}