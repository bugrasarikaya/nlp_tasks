import urllib.request
url="http://www.physics.metu.edu.tr/~uoyilmaz/TurkSiiri/cagdasturksiiri/sukruerbas/SukruErbas-(Koyluleri...).htm"
connection=urllib.request.urlopen(url)
data=connection.read().decode('windows-1254')
import re
context=re.sub('<[^<]+?>', '', data)
context=context.replace('&nbsp;','')
context=" ".join(context.split())
context=context.lower()
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
clean_context=""
for char in context:
    if char not in punctuations:
        clean_context=clean_context+char
from nltk.tokenize import word_tokenize
tokens=word_tokenize(clean_context)
import simplemma
langdata=simplemma.load_data('tr')
lemmas=[]
for token in tokens:
    lemmas.append(simplemma.lemmatize(token,langdata))
from nltk.util import ngrams
bigrams=ngrams(lemmas, 2)
trigrams=ngrams(lemmas, 3)
import pandas
import matplotlib.pyplot
matplotlib.pyplot.figure(1)
bigrams_series=(pandas.Series(bigrams).value_counts())[:10]
bigrams_series.sort_values().plot.barh(color="maroon", width=.8, figsize=(7, 4))
matplotlib.pyplot.gcf().subplots_adjust(left=0.2)
matplotlib.pyplot.figure(2)
trigrams_series=(pandas.Series(trigrams).value_counts())[:10]
trigrams_series.sort_values().plot.barh(color="maroon", width=.8, figsize=(7, 4))
matplotlib.pyplot.gcf().subplots_adjust(left=0.3)
matplotlib.pyplot.show()
