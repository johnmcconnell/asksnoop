import src.freebase.FreebaseAPI as freebase
import src.models.okapi as okapi

def score(query):
    noun = factcheck_helper(query)
    qtopic = freebase.most_likely_topic(noun)
    topic = freebase.get_full_topic(qtopic['mid'])
    brief = freebase.topic_summary(topic)
    return okapi.okapi(query,brief)
