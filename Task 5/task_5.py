from urllib.request import Request, urlopen
url = "https://khosann.com/askin-insan-ustun-insana-karsi/"
req = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
web_page = urlopen(req).readlines()
found = False
content = ""
for line in web_page:
    line = line.decode("utf-8")
    if '<h1>' in line or '<h2>' in line or '<p>' in line and not '</aside>' in line: content += line
import re
clean_content = re.sub("<[^<]+?>", "", content)
clean_content = re.sub("[\(\[].*?[\)\]]", "", clean_content)
clean_content = clean_content.replace("&#8230;", "...")
clean_content = clean_content.replace("&#8220;", '"')
clean_content = clean_content.replace("&#8221;", '"')
clean_content = clean_content.replace("&#8217;", "'")
clean_content = clean_content.replace("“", '"')
clean_content = clean_content.replace("”", '"')
clean_content = clean_content.replace("’", "'")
clean_content = clean_content.replace("I", "ı")
clean_content = clean_content.replace("İ", "i")
clean_content = clean_content.lower()
clean_content = ' '.join(clean_content.split())
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
clean_content_no_punctuation = ""
for char in  clean_content:
    if char not in punctuations: clean_content_no_punctuation += char
import simplemma
from simplemma import text_lemmatizer
lemmas = text_lemmatizer(clean_content_no_punctuation, simplemma.load_data('tr'))
from urllib.request import Request, urlopen
url = "https://raw.githubusercontent.com/ahmetax/trstop/master/dosyalar/turkce-stop-words"
req = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
web_page = urlopen(req).readlines()
stop_words = []
for line in web_page:
    line = line.decode("utf-8")
    line = line.replace("\n", "")
    stop_words.append(line)
clean_lemmas = []
for lemma in lemmas:
    if lemma not in stop_words and not lemma.isnumeric():
        numericless_lemma = ""
        for char in lemma:
            if not char.isnumeric(): numericless_lemma += char
        clean_lemmas.append(numericless_lemma)
import pandas
pandas.set_option("display.max_rows", None)
print("%-15s%s" %("Word", "Count"))
print(pandas.Series(clean_lemmas).value_counts())
from nltk.util import ngrams
bigrams = ngrams(clean_lemmas, 2)
trigrams = ngrams(clean_lemmas, 3)
import matplotlib.pyplot
matplotlib.pyplot.figure(1).suptitle("Bigrams")
bigrams_series = (pandas.Series(bigrams).value_counts())[:5]
bigrams_series.sort_values().plot.barh(color = "maroon", width = .8, figsize = (7, 4))
matplotlib.pyplot.gcf().subplots_adjust(left = 0.2)
matplotlib.pyplot.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(integer = True))
matplotlib.pyplot.figure(2).suptitle("Trigrams")
trigrams_series = (pandas.Series(trigrams).value_counts())[:5]
trigrams_series.sort_values().plot.barh(color = "maroon", width = .8, figsize = (7, 4))
matplotlib.pyplot.gcf().subplots_adjust(left = 0.3)
matplotlib.pyplot.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(integer = True))
matplotlib.pyplot.show()
from nltk.tokenize import sent_tokenize
sentences = sent_tokenize(clean_content)
sentences_no_punctuation = []
for sentence in sentences:
    sentence_no_punctuation = ""
    for char in sentence:
        if char not in punctuations: sentence_no_punctuation += char
    sentences_no_punctuation.append(sentence_no_punctuation)
import simplemma
lemmatized_sentences = []
for sentence in sentences_no_punctuation:
    sentence_lemmas = text_lemmatizer(sentence, simplemma.load_data('tr'))
    lemmatized_sentence = ""
    for lemma in sentence_lemmas:
        if lemma not in stop_words and not lemma.isnumeric():
            numericless_lemma = ""
            for char in lemma:
                if not char.isnumeric(): numericless_lemma += char
            lemmatized_sentence += numericless_lemma + " "
    lemmatized_sentence = lemmatized_sentence[:-1]
    lemmatized_sentences.append(lemmatized_sentence)
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(min_df = 1)
dtm = vectorizer.fit_transform(lemmatized_sentences)
from sklearn.decomposition import TruncatedSVD
lsa = TruncatedSVD(1, algorithm = 'randomized')
dtm_lsa = lsa.fit_transform(dtm)
df = pandas.DataFrame(lsa.components_,index = ["component_1"], columns = vectorizer.get_feature_names())
for i in range(len(df.columns) - 1):
    for j in range(i + 1, len(df.columns)):
        difference = abs(df.iloc[0][i] - df.iloc[0][j])
        if i == 0 and j == 1: minimum = difference
        if difference < minimum:
            minimum = difference
            index_i = i
            index_j = j
print("The most similar two words: " + df.columns[index_i] + " - " + df.columns[index_j])
