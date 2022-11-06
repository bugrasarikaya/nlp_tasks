from urllib.request import Request, urlopen
url = "http://www.gutenberg.org/files/11/11-0.txt"
from nltk.tokenize import sent_tokenize, word_tokenize
req = Request(url, headers = {"User-Agent": "Mozilla/5.0"})
web_page = urlopen(req).readlines()
lines = []
for line in web_page:
    line = line.decode("utf-8-sig")
    line = line.replace("\r\n", " ")
    line = line.replace("“", '"')
    line = line.replace("”", '"')
    line = line.replace("’", "'")
    line = line.replace("—", "-")
    lines.append(line)
content = ""
for line in lines:
    content += line
content += input("Enter a sentence: ")
from nltk.tokenize import sent_tokenize,  word_tokenize
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
data = []
for sentence in sent_tokenize(content):
    clean_sentence = ""
    for char in sentence.lower():
        if char not in punctuations: clean_sentence += char
    data.append(clean_sentence)
from sklearn.feature_extraction.text import CountVectorizer
count_vectorizer = CountVectorizer(stop_words = "english")
sparse_matrix = count_vectorizer.fit_transform(data)
doc_term_matrix = sparse_matrix.todense()
from sklearn.metrics.pairwise import cosine_similarity
max_similarity_score = 0
most_similar_sentence_index = -1
for index in range(len(data) - 1):
    similarity_score = cosine_similarity(sparse_matrix[index], sparse_matrix[len(data) - 1])
    if similarity_score > max_similarity_score:
        max_similarity_score = similarity_score
        most_similar_sentence_index = index
if most_similar_sentence_index == -1: print("Failure")
else:
    print("Most similar sentence: '" + data[most_similar_sentence_index] + "'")
    print("Similarity score: " + str(float(max_similarity_score)))
