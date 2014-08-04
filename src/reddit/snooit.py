import praw

RESULT_LIMIT = 10

user_agent = ('AskSnoo 1.0 by /u/asksnoo  github.com/johnmcconnell/asksnoop')
r = praw.Reddit(user_agent=user_agent)
user_name = 'asksnoo'
user = r.get_redditor(user_name)
gen = r.get_front_page(limit=RESULT_LIMIT)

SUBREDDIT_URL = 'http://www.reddit.com/r/'
TIL = 'todayilearned'
ELI5 = 'explainlikeimfive'
ALL = 'all'

def get_submission_type(submission):
    if submission.selftext > 0:
        return 'text'
    else:
        if 'http://www.reddit.com' == submission.url[0: 21]:
            return 'text'
        else:
            return 'link'

def get_submission_content(submission):
    if get_submission_type(submission) == 'text':
        return submission.selftext
    else:
        return submission.url

def get_hot_post_titles(subreddit, limit):
    hots = r.get_subreddit(subreddit).get_hot(limit=limit)

    # skip the welcome post
    next(hots)

    titles = []
    for hot in hots:
	titles.append(hot.title)
    return titles
