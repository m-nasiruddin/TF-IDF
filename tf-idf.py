#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 20:01:55 2018

@author: osboxes
"""

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
import string
from collections import Counter

# tokenization in NLTK
def get_tokens():
   with open('shakes1.txt', 'r') as shakes:
    text = shakes.read()
    lowers = text.lower()
    # remove the punctuation using the character deletion step of translate
    no_punctuation = lowers.translate(string.punctuation)
    tokens = nltk.word_tokenize(no_punctuation)
    return tokens

tokens = get_tokens()
count = Counter(tokens)
print (count.most_common(10))

# stop word removal
# nltk.download('stopwords')
tokens = get_tokens()
filtered = [w for w in tokens if not w in stopwords.words('english')]
count = Counter(filtered)
print (count.most_common(100))

# stemming using NLTK
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

stemmer = PorterStemmer()
stemmed = stem_tokens(filtered, stemmer)
count = Counter(stemmed)
print (count.most_common(100))
