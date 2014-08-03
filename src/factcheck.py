import sys
import os
from nltk import *
from nltk.parse import *

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
#text
def check(text):
	#text = "TIL the Fibonacci Sequence was described by an Indian mathematician ~1200 years before Fibonacci wrote of it"
	#text = "TIL George Washington was a Physicist"
	text = text.replace("TIL","")
	#get text(eventually from reddit post titles)

	#Tokenize
	tokens = word_tokenize(text)
	print "\ntokenization of text:\n",tokens
	#POS tagging
	#tags = pos_tag(tokens)
	#print "\nPOS-Tagging:\n",tags
	#Chunking
	#chunks = chunk.ne_chunk(tags)
	#print "\nchunking:\n", chunks
	#pieces = []
	#for i in tags:
	#	if "NN" in i[1]:
	#		pieces.append(i[0])
	#print pieces
	#return pieces
	
	query = []
	os.popen("echo '"+text+"' > ~/stanfordtemp.txt")
	parser_out = os.popen("~/asksnoop/src/stanford-parser-2012-11-12/lexparser.sh ~/stanfordtemp.txt").readlines()
	#print parser_out
	flag = False
	for parse in parser_out:
		print parse
	print "Filter out only Noun Phrase"
	for parse in parser_out:
		if "NP" in parse:
			print parse
			for word in tokens:
				if word in parse:
					query.append(word)
					flag = True
		if flag:
			break
	print query
	return " ".join(query)
	#bracketed_parse = " ".join( [i.strip() for i in parser_out if i.strip()[0] == "("] )
	#print bracketed_parse
	


#string holding the fact query we want to check
"""query = ""

for i in range(len(sys.argv)):
	query = sys.argv[i]

check(query)"""
check()
"""
Notes:
Penn Treebank seems to have a good POS Tag set (used above) and Stanford uses parts of it for its' parser.
I still think trying to get the Stanford parser to work through nltk is the best way to go, but
otherwise I was unable to find a good solution this morning...

Penn Treebank POS_Tag Labels
https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html

If you can't get the parser to work, we can just extract groupings of Nouns or Dates from the chunker, 
assuming we are limiting our data to simple sentences

Other information I've been looking at:

Stanford parser info:
http://nlp.stanford.edu/software/lex-parser.shtml
The Parser
http://nlp.stanford.edu:8080/corenlp/process
Paper on dependency parses
http://nlp.stanford.edu/pubs/LREC06_dependencies.pdf

NLTK Documentation (modules)
http://www.nltk.org/index.html
PDF Book
http://www.nltk.org/book/

"""

	
