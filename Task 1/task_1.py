latin_text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
latin_text=latin_text.lower()
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
clean_latin_text=""
for char in latin_text:
    if char not in punctuations:
        clean_latin_text=clean_latin_text+char
from cltk import NLP
cltk_nlp = NLP(language="lat")
cltk_doc=cltk_nlp.analyze(text=clean_latin_text)
print("CLTK")
print("Token - Lemma:")
for token, lemma in zip(cltk_doc.tokens, cltk_doc.lemmata):
    print (token," - ",lemma)
print()
import simplemma
langdata = simplemma.load_data('la')
from simplemma import simple_tokenizer
from simplemma import text_lemmatizer
print("Simplemma")
print("Token - Lemma:")
for token, lemma in zip(simple_tokenizer(clean_latin_text), text_lemmatizer(clean_latin_text,langdata)):
    print (token," - ",lemma)
