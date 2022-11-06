file = open("tur_news_2019_100K-sentences.txt", encoding = "utf-8")
from nltk.tokenize import word_tokenize
tokens = word_tokenize(file.read())
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~''' + "“”’…"
clean_tokens = []
symbolic = False
for token in tokens:
    for char in token:
        if char in punctuations: symbolic = True
        else:
            symbolic = False
            break
    if not symbolic: clean_tokens.append(token)
token_freqs = {}
for token_1 in clean_tokens:
    if token_1 not in token_freqs:
        count = 0
        for token_2 in clean_tokens:
            if token_1 == token_2: count += 1
        token_freqs[token_1] = count
threshold = 5
uncommon_tokens = []
common_tokens = []
for key, value in token_freqs.items():
    if value <= threshold: uncommon_tokens.append(key)
    else: common_tokens.append(key)
def jaccard(word_1, word_2):
    intersection = len(list(set(word_1).intersection(word_2)))
    union = (len(word_1) + len(word_2)) - intersection
    return float(intersection) / union
token_correction_table = {}
for uncommon_token in uncommon_tokens:
    max_similarity_score = 0
    incorrect_token = False
    correct_token = False
    for common_token in common_tokens:
        similarity_score = jaccard(uncommon_token, common_token)
        if similarity_score > max_similarity_score and similarity_score > 0.77:
            max_similarity_score = similarity_score
            incorrect_token = uncommon_token
            correct_token = common_token
    if incorrect_token and correct_token: token_correction_table[incorrect_token] = correct_token
for key, value in token_correction_table.items():
    print(key + " - " + value)
