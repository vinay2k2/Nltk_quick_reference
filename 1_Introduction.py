#All the code in this repository has been tried and tested on Ubuntu 14.04
# Every section has been written independently and hence you can start at any section/task you want to learn
# To install nltk: sudo pip install -U nltk
# If you are behind proxy try:sudo -E pip install -U nltk
# Once installed go to terminal ctrl+alt+t
# Type python to go to python interactive shell or you could use gedit filename.py to save your work
# for later or even you could install other #editor like sublime
################### Section 1: Getting Started with NLTK: Tokenization ####################
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
text="I am going to learn NLTK and this is going to be awesome.I can use this code for later reference. In fact anyone can use this code for quick reference"
#Get all the sentences in the text separator is '.'
tokenized_sentences=sent_tokenize(text)
#Get all the words in the text here separator is space
tokenized_words=word_tokenize(text)
print tokenized_sentences
print tokenized_words
