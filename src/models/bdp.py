# query = sentence to be validated
# document = something established to be true

import helper

def get_bdp(query, document):

    stopped_query = helper.get_non_stop_words(query)
    stopped_document = helper.get_non_stop_words(document)

    score = 0
    for word in stopped_query:
        if word in stopped_document:
            score += 1

    score = float(score) / len(query)
    return score

print get_bdp("George Washington is Canadian".split(), "George Washington is American".split())



