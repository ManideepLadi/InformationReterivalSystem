import time
from nltk import word_tokenize

sentence1="what similarity laws must be obeyed when constructing aeroelastic models of heated high speed aircraft "
sentence2="what similarity laws must be obeyed when constructing aeroelastic models of heated high speed aircraft "

start1 = time.time()
sentence1.split()
print('str.split():\t', time.time() - start1)


start2 = time.time()
word_tokenize(sentence2)
print('word_tokenize():\t', time.time() - start2)
