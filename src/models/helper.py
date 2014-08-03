# helper functions for the models

import stopwords

def get_word_count(words):
    counts = {}
    for word in words:
        if counts.has_key(word):
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def get_non_stop_words(words):
    # make a copy
    result = list(words)

    for word in words:

        if word in stopwords.STOPWORDS:
            result.remove(word)

    return result


# words = ["during", "each", "either", "manbearpig"]
# print get_non_stop_words(words)


