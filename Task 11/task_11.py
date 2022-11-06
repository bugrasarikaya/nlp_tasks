import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
text = "There are many techniques available to generate extractive summarization to keep it simple, I will be using an unsupervised learning approach to find the sentences similarity and rank them. Summarization can be defined as a task of producing a concise and fluent summary while preserving key information and overall meaning. One benefit of this will be, you don’t need to train and build a model prior start using it for your project. It’s good to understand Cosine similarity to make the best use of the code you are going to see. Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space that measures the cosine of the angle between them. Its measures cosine of the angle between vectors. The angle will be 0 if sentences are similar."
stop_words = set(stopwords.words("english"))
words = word_tokenize(text)
freq_table = dict()
for word in words:
    word = word.lower()
    if word in stop_words:
        continue
    if word in freq_table:
        freq_table[word] += 1
    else:
        freq_table[word] = 1
sentences = sent_tokenize(text)
sentence_value = dict()
for sentence in sentences:
    for word, freq in freq_table.items():
        if word in sentence.lower():
            if sentence in sentence_value:
                sentence_value[sentence] += freq
            else:
                sentence_value[sentence] = freq
sum_values = 0
for sentence in sentence_value:
    sum_values += sentence_value[sentence]
average = int(sum_values / len(sentence_value))
summary = ""
for sentence in sentences:
    if (sentence in sentence_value) and (sentence_value[sentence] > (1.2 * average)):
        summary += sentence + " "
print(summary)
