import src.freebase.FreebaseAPI as freebase
import src.models.okapi as okapi
import src.localapi as lapi

def score(query):
    noun = lapi.noun_phrase(query)
    qtopic = freebase.most_likely_topic(noun)
    topic = freebase.get_full_topic(qtopic['mid'])
    brief = freebase.topic_summary(topic)
    return okapi.okapi(query,brief)
