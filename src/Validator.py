import src.freebase.FreebaseAPI as freebase
import src.models.okapi as okapi
import src.localapi as lapi
import src.models.helper as helper
import logging

def noun(query):
    return lapi.noun_phrase(query)

def topic(noun):
    qtopic = freebase.most_likely_topic(noun)
    topic = freebase.get_full_topic(qtopic['mid'])
    return (topic, qtopic['name'])

def score(query,topic):
    brief = freebase.topic_summary(topic)
    query = helper.get_non_stop_words(query.split())
    brief = helper.get_non_stop_words(brief.split())
    logging.info(query)
    logging.info(brief)
    return okapi.okapi(query,brief)
