from newspaper import Article
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import string
nltk.download('vader_lexicon')
url1 = 'https://www.cbsnews.com/live-updates/trump-us-capitol-secured-dc-protest/'
articleCBS = Article(url1)
articleCBS.download()
articleCBS.parse()
CBStext = articleCBS.text
url2 = 'https://www.foxnews.com/politics/how-wednesdays-capitol-riot-come-to-fruition'
articleFox = Article(url2)
articleFox.download()
articleFox.parse()
Foxtext = articleFox.text

stopWords = ['a','the','and','an','this','how','why','would','could','For','The']

def analyze(articleText, name):
    score = SentimentIntensityAnalyzer().polarity_scores(articleText)
    print(f'The news for {name} score is: {score}')

    wordlist = articleText.split()
    strippables = string.punctuation + string.whitespace

    wordfreq = []

    for w in wordlist:
        w = w.strip(strippables)
        w = w.lower()
        if w not in stopWords:
            wordfreq.append(wordlist.count(w))
    
    totalFreq= str(list(zip(wordlist, wordfreq)))

    return totalFreq



def sortlist(totalFreq):
    sorted = [(totalFreq[1], key) for key in totalFreq]
    sorted.sort()

    return sorted



print(analyze(Foxtext, 'Fox'))
print(analyze(CBStext, 'CBS'))
# print(analyzeFox())
# print(sortlist(totalFreqFox))
#print(removeStopWords(totalFreqCBS, stopWords))

