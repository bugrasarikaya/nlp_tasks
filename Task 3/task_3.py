import urllib.request
url = "http://shakespeare.mit.edu/romeo_juliet/full.html"
connection = urllib.request.urlopen(url)
data = connection.readlines()
clean_data = ""
for line in data:
    line = line.decode("windows-1254")
    if "<i>" not in line:
        if "                  " in line:
            line = ' '.join(line.split())
            line = line[17:] + '\n'
        clean_data = clean_data + line
import re
clean_data = re.sub("<[^<]+?>", "", clean_data)
clean_data = re.sub("[\(\[].*?[\)\]]", "", clean_data).split('\n')
romeo = ""
juliet = ""
for line_index in range(len(clean_data)):
    if "ROMEO" in clean_data[line_index]:
        line_index = line_index + 1
        while not (not clean_data[line_index] and not clean_data[line_index + 1]):
            romeo = romeo + clean_data[line_index] + '\n'
            line_index = line_index + 1
    elif "JULIET" in clean_data[line_index]:
        line_index = line_index + 1
        while not (not clean_data[line_index] and not clean_data[line_index + 1]):
            juliet = juliet + clean_data[line_index] + '\n'
            line_index = line_index + 1
romeo = romeo.lower()
juliet = juliet.lower()
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
clean_romeo = ""
clean_juliet = ""
for char in romeo:
    if char not in punctuations: clean_romeo = clean_romeo + char
for char in juliet:
    if char not in punctuations: clean_juliet = clean_juliet + char
import nltk
romeo_tokens = nltk.word_tokenize(clean_romeo)
juliet_tokens = nltk.word_tokenize(clean_juliet)
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
filtered_romeo_tokens = []
filtered_juliet_tokens = []
for token in romeo_tokens:
    if token not in stop_words: filtered_romeo_tokens.append(token)
for token in juliet_tokens:
    if token not in stop_words: filtered_juliet_tokens.append(token)
romeo_tokens_count = len(filtered_romeo_tokens)
juliet_tokens_count = len(filtered_juliet_tokens)
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
romeo_lemmas = []
juliet_lemmas = []
for token in filtered_romeo_tokens: romeo_lemmas.append(wordnet_lemmatizer.lemmatize(token))
for token in filtered_juliet_tokens: juliet_lemmas.append(wordnet_lemmatizer.lemmatize(token))
from nltk.util import ngrams
bigrams_romeo = ngrams(romeo_lemmas, 2)
bigrams_juliet = ngrams(juliet_lemmas, 2)
trigrams_romeo = ngrams(romeo_lemmas, 3)
trigrams_juliet = ngrams(juliet_lemmas, 3)
from nltk import pos_tag
romeo_pos_tags = pos_tag(filtered_romeo_tokens)
juliet_pos_tags = pos_tag(filtered_juliet_tokens)
from nltk import pos_tag
import pandas, matplotlib, matplotlib.pyplot
from matplotlib.ticker import MaxNLocator
matplotlib.pyplot.figure(1).suptitle("Romeo Bigrams in " + str(romeo_tokens_count) + " Tokens")
bigrams_series_romeo = (pandas.Series(bigrams_romeo).value_counts())[:20]
bigrams_series_romeo.sort_values().plot.barh(color = "maroon", width = .8, figsize = (7, 4))
matplotlib.pyplot.gcf().subplots_adjust(left = 0.2)
matplotlib.pyplot.figure(2).suptitle("Juliet Bigrams in " + str(juliet_tokens_count) + " Tokens")
bigrams_series_juliet = (pandas.Series(bigrams_juliet).value_counts())[:20]
bigrams_series_juliet.sort_values().plot.barh(color = "maroon", width = .8, figsize = (7, 4))
matplotlib.pyplot.gcf().subplots_adjust(left = 0.2)
matplotlib.pyplot.figure(3).suptitle("Romeo Trigrams in " + str(romeo_tokens_count) + " Tokens")
trigrams_series_romeo = (pandas.Series(trigrams_romeo).value_counts())[:20]
trigrams_series_romeo.sort_values().plot.barh(color = "maroon", width = .8, figsize = (7, 4))
matplotlib.pyplot.gcf().subplots_adjust(left = 0.3)
matplotlib.pyplot.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(integer=True))
matplotlib.pyplot.figure(4).suptitle("Juliet Trigrams in " + str(juliet_tokens_count) + " Tokens")
trigrams_series_juliet = (pandas.Series(trigrams_juliet).value_counts())[:20]
trigrams_series_juliet.sort_values().plot.barh(color = "maroon", width = .8, figsize = (7, 4))
matplotlib.pyplot.gcf().subplots_adjust(left = 0.3)
matplotlib.pyplot.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(integer=True))
matplotlib.pyplot.figure(5).suptitle("Romeo POS Tags in " + str(romeo_tokens_count) + " Tokens")
pos_tags_series_romeo = (pandas.Series([i[1] for i in romeo_pos_tags]).value_counts())[:20]
pos_tags_series_romeo.sort_values().plot.barh(color = "maroon", width = .8, figsize = (7, 4))
matplotlib.pyplot.gcf().subplots_adjust(left = 0.2)
matplotlib.pyplot.figure(6).suptitle("Juliet POS Tags in " + str(juliet_tokens_count) + " Tokens")
pos_tags_series_juliet = (pandas.Series([i[1] for i in juliet_pos_tags]).value_counts())[:20]
pos_tags_series_juliet.sort_values().plot.barh(color = "maroon", width = .8, figsize = (7, 4))
matplotlib.pyplot.gcf().subplots_adjust(left = 0.2)
matplotlib.pyplot.show()
