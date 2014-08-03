# query = sentence to be validated
# document = something established to be true

import math
import helper

def okapi(query, document):
    k1 = 1.5
    k3 = 300
    b = 0.2

    N = 1
    n = len(document)
    n_avg = n

    cwds = helper.get_word_count(document)
    cwqs = helper.get_word_count(query)

    summation = 0
    for word in query:
        if word in document:
            df = 1
	    doc_count = cwds[word]
        else:
            df = 0
	    doc_count = 0
	query_count = 1

        first = 1 #math.log((N - df + 0.5)/(df + 0.5))
        second = ((k1 + 1) * doc_count)/(k1 * (1 - b + (b * (n / n_avg))) + doc_count)
        third = ((k3 + 1) * query_count)/(k3 + query_count)

        summation += first * second * third

    return summation

print okapi('This is a completely factual statement'.split(),
	'This is another completely factual statement'.split())
print okapi('I found a dog near the park'.split(),
	'This is another completely factual statement'.split())
print okapi('completely factual'.split(),
	'This is another completely factual statement'.split())
