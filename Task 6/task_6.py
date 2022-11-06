import simplemma
from simplemma import simple_tokenizer
from simplemma import text_lemmatizer
langdata = simplemma.load_data('tr')
from urllib.request import Request, urlopen
url = "https://raw.githubusercontent.com/ahmetax/trstop/master/dosyalar/turkce-stop-words"
req = Request(url, headers = {"User-Agent": "Mozilla/5.0"})
web_page = urlopen(req).readlines()
stop_words = []
for line in web_page:
    line = line.decode("utf-8")
    line = line.replace("\n", "")
    stop_words.append(line)
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
def normalize_content(content):
    clean_content = ""
    for char in content:
        if char not in punctuations: clean_content += char
    clean_content = clean_content.replace('I', 'ı')
    clean_content = clean_content.lower()
    clean_content_lemmas = text_lemmatizer(clean_content, langdata)
    clean_content_lemmas_no_stop_word = []
    for lemma in clean_content_lemmas:
        if lemma not in stop_words: clean_content_lemmas_no_stop_word.append(lemma)
    return clean_content_lemmas_no_stop_word
def lesk(word, sentence):
    max_overlap = 0
    sentence_lemmas = normalize_content(sentence)
    for sense_index in dictionary[word]:
        sense_lemmas = normalize_content(dictionary[word][sense_index])
        overlap = 0
        for sense_lemma in sense_lemmas:
            for sentence_lemma in sentence_lemmas:
                if sense_lemma == sentence_lemma: overlap += 1
        if overlap > max_overlap:
            max_overlap = overlap
            determined_sense_index = sense_index
    return dictionary[word][determined_sense_index]
sentence = "Fazla tevazunun sonu, vasat insandan nasihat dinlemektir."
dictionary = {"vasat": {1: "orta kalitede insan", 2: "ortam fazla insan nasihat"}}
print(lesk("vasat", sentence))
