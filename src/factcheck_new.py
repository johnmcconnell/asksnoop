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
def remove_tags(parse_branch):
	words = parse_branch.replace("(CC","")
	words = words.replace("(CD","")
	words = words.replace("(DT","")
	words = words.replace("(EX","")
	words = words.replace("(FW","")
	words = words.replace("(IN","")
	words = words.replace("(JJR","")
	words = words.replace("(JJS","")
	words = words.replace("(JJ","")
	words = words.replace("(LS","")
	words = words.replace("(MD","")
	words = words.replace("(NNPS","")
	words = words.replace("(NNS","")
	words = words.replace("(NNP","")
	words = words.replace("(NP","")
	words = words.replace("(NN","")
	words = words.replace("(PDT","")
	words = words.replace("(POS","")
	words = words.replace("(PRP$","")
	words = words.replace("(PRP","")
	words = words.replace("(P","")
	words = words.replace("(RB","")
	words = words.replace("(RBR","")
	words = words.replace("(RBS","")
	words = words.replace("(RP","")
	words = words.replace("(SYM","")
	words = words.replace("(TO","")
	words = words.replace("(UH","")
	words = words.replace("(VBD","")
	words = words.replace("(VBG","")
	words = words.replace("(VBN","")
	words = words.replace("(VBP","")
	words = words.replace("(VBZ","")
	words = words.replace("(VB","")
	words = words.replace("(WDT","")
	words = words.replace("(WP$","")
	words = words.replace("(WP","")
	words = words.replace("(WRB","")
	words = words.replace("\n","")
	words = words.replace("   ","")
	words = words.replace(")","")
	return words
#text
def check(text):
	text = "TIL the Fibonacci Sequence was described by an Indian mathematician ~1200 years before Fibonacci wrote of it"
	#text = "TIL George Washington was a Physicist"
	text = text.replace("TIL","")
	
	query = []
	os.popen("echo '"+text+"' > ~/stanfordtemp.txt")
	parser_out = os.popen("~/asksnoop/src/stanford-parser-2012-11-12/lexparser.sh ~/stanfordtemp.txt").readlines()
	print "Parsing text:'",text,"'\n"
	print type(parser_out)
	for parse in parser_out:
		print parse
	

	print "Filtering out only Noun Phrase"
	phrases = []
	for parse in parser_out:
		if "NP" in parse:
			print "original",parse
			phrase = remove_tags(parse)
			print "cleaned phrase:",phrase,"\n"
			phrases.append(phrase)

	print phrases
	return phrases
	
	


#string holding the fact query we want to check
#query = ""

#for i in range(len(sys.argv)):
	#query = sys.argv[i]

#query = "TIL George Washington was a Physicist"
check("test")
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

	
