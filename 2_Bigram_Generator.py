#This code can generate bigrams for all the sentences from any text file
#Author: Vinay Kumar (vinay2k2)
#Dated: 20.11.2016
import nltk
from nltk.tokenize import word_tokenize
#Output File name
out_ref=open("output.txt","a")
for line in open("input.txt","r").readlines():
      # Temporary list of all words 
      l=word_tokenize(line)
      # generates Bigram
      #This is called python comprehension here we get the index values and just use those to get consecutive words
      #See LOGICAL_EXAMPLE below if following line doesn't make sense to you
      list= [ " ".join([l[index],l[index+1]]) for index,value in enumerate(l) if index<len(l)-1]
      #Convert list item to string and write
      for item in list:
           out_ref.write("".join(item))
           out_ref.write("\n")
#END_OF_CODE_SECTION         
           
           
 '''          
LOGICAL_EXAMPLE:
>>> line="This is my sentence"
>>> l=word_tokenize(line)
>>> l
['This', 'is', 'my', 'sentence']
>>> list=[]
>>> for index,value in enumerate(l):
	if index<len(l)-1:
		items_to_append=[l[index],l[index+1]]
		list.append(" ".join(items_to_append)
>>> list
['This is', 'is my', 'my sentence']
'''
