import src.freebase.FreebaseAPI as freebase
import src.models.okapi as okapi
import src.localapi as lapi
import src.models.helper as helper
import logging

def nouns(query):
    return lapi.noun_phrases(query)

def topic(noun):
    qtopic = freebase.most_likely_topic(noun)
    topic = freebase.get_full_topic(qtopic['mid'])
    return (topic, qtopic['name'])

def score(query,topics):
    brief = []
    for topic in topics:
    	raw = freebase.topic_summary(topic).split()
	brief += helper.get_non_stop_words(raw)
    query = helper.get_non_stop_words(query.split())
    logging.info(brief)
    return okapi.okapi(query,brief)
