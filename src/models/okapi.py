# query = sentence to be validated
# document = something established to be true

from sets import Set
import math

def okapi(query, document):
    k1 = 1.5
    k3 = 500 
    b = 0.5

    q_words = query.split()
    d_words = document.split()

    N = 1
    n = len(d_words)
    n_avg = n

    cwds = {}
    for word in d_words:
        if cwds.has_key(word):
            cwds[word] += 1;
        else:
            cwds[word] = 1

    for word in q_words:
        if word not in d_words:
            cwds[word] = 0

    cwqs = {}
    for word in q_words:
        if cwqs.has_key(word):
            cwqs[word] += 1;
        else:
            cwqs[word] = 1       

    for word in d_words:
        if word not in q_words:
            cwqs[word] = 0

    union_words = set(q_words)
    union_words.update(d_words)

    summation = 0

    for word in union_words:
        if word in d_words:
            df = 1
        else:
            df = 0

        first = math.log((N - df + 0.5)/(df + 0.5))
        second = ((k1 + 1) * cwds[word])/(k1 * (1 - b + (b * (n / n_avg))) + cwds[word])
        third = ((k3 + 1) * cwqs[word])/(k3 + cwqs[word])

        summation += first * second * third

    return summation


print okapi('hello there bob', 'hello there jim')
