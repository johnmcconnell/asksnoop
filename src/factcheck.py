import sys
import os
from nltk import *
from nltk.parse import *
from nltk.parse import stanford

"""
This code takes in a question from reddit and checks its' factual information with the freebase database through NLP

uses NLTK and associated tools
Penntree's POS_Tagging
NLTK's chunking code

Outline:
Use Reddit API to get list of post titles as input sentences
pass them through check()
which returns relevent tagged/chunked term(s)
Use term(s) to query Freebase API
get most relevant page
scan page and evaluate relevance/correctness to terms



"""

def check():
	#get text(eventually from reddit post titles)
	#text = statement
	grammar = data.load('grammars/large_grammars/atis.cfg')
	
	text = "George Washington was the first president of the United States of America"
	#Capitalization matters in distinguishing from nouns/verbs
	#text = text.lower()

	#Tokenize
	token = word_tokenize(text)
	print "\ntokenization of text:\n",token
	#POS tagging
	postag = pos_tag(token)
	print "\nPOS-Tagging:\n",postag
	#Chunking
	entities = chunk.ne_chunk(postag)
	print "\nchunking:\n", entities
	#os.popen("echo '" + text + "' > ~/stanfordtemp.txt")
	#parser_out = os.popen("~/stanford-parser-2012-11-12/lesparser.sh ~/stanfordtemp.txt").readlines()
	#parser = stanford.StanfordParser(model_path = "edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
	#parser.raw_parse_sents(text)

	os.popen("echo '"+text+"' > ~/stanfordtemp.txt")
	parser_out = os.popen("~/asksnoop/src/handlers/stanford-parser-2012-11-12/lexparser.sh ~/stanfordtemp.txt").readlines()
	
	bracketed_parse = " ".join( [i.strip() for i in parser_out if i.strip()[0] == "(" and len(i.strip()) > 0] )
	print bracketed_parse
	
check()
	
