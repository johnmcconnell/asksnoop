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

def check():
	#get text(eventually from reddit post titles)
	#text = statement
	
	
	text = "the declaration of indepenedence was signed in 1776"
	#Capitalization matters in distinguishing from nouns/verbs
	#text = text.lower()

	#Tokenize
	tokens = word_tokenize(text)
	print "\ntokenization of text:\n",tokens
	#POS tagging
	tags = pos_tag(tokens)
	print "\nPOS-Tagging:\n",tags
	#Chunking
	chunks = chunk.ne_chunk(tags)
	print "\nchunking:\n", chunks
	
	grammar = data.load('grammars/large_grammars/atis.cfg')


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
###below code from http://streamhacker.com/2008/12/29/how-to-train-a-nltk-chunker/ (doesn't seem to work properly)
	print conll_tag_chunks(tags)
import nltk.chunk
 	
def conll_tag_chunks(chunk_sents):
    tag_sents = [nltk.chunk.tree2conlltags(tree) for tree in chunk_sents]
    return [[(t, c) for (w, t, c) in chunk_tags] for chunk_tags in tag_sents]
	
import nltk.corpus, nltk.tag
 
def ubt_conll_chunk_accuracy(train_sents, test_sents):
    train_chunks = conll_tag_chunks(train_sents)
    test_chunks = conll_tag_chunks(test_sents)
 
    u_chunker = nltk.tag.UnigramTagger(train_chunks)
    print 'u:', nltk.tag.accuracy(u_chunker, test_chunks)
 
    ub_chunker = nltk.tag.BigramTagger(train_chunks, backoff=u_chunker)
    print 'ub:', nltk.tag.accuracy(ub_chunker, test_chunks)
 
    ubt_chunker = nltk.tag.TrigramTagger(train_chunks, backoff=ub_chunker)
    print 'ubt:', nltk.tag.accuracy(ubt_chunker, test_chunks)
 
    ut_chunker = nltk.tag.TrigramTagger(train_chunks, backoff=u_chunker)
    print 'ut:', nltk.tag.accuracy(ut_chunker, test_chunks)
 
    utb_chunker = nltk.tag.BigramTagger(train_chunks, backoff=ut_chunker)
    print 'utb:', nltk.tag.accuracy(utb_chunker, test_chunks)
 

check()
	
