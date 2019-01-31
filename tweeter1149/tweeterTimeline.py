import twitter
from tweeter1149 import tweeterKey
api = twitter.Api()

'''
open tweeter developer account and all keys
replace all api key with yours
api_keys = {"consumer_key": "AJKDbsdfsds",
           "consumer_secret": "Ajhshgdshg",
           "access_token": "NFSUIGuogy",
           "access_token_secret": "FCGHJJBDHOJKHfgjh"
           }
'''


# users = api.GetFriends()
# print([u.name for u in users])
# print(users[0])

print('=======================')
# user1 = "realDonaldTrump"
# screen_name = user1
# statuses = api.GetUserTimeline(screen_name=screen_name,count=2)
# print([s.text for s in statuses])
# print(statuses)

def tweet_timeline(user_name, count):
    api_keys = tweeterKey.api_keys()
    api = twitter.Api(consumer_key=api_keys['consumer_key'][:-1],
                      consumer_secret=api_keys['consumer_secret'][:-1],
                      access_token_key=api_keys['access_token'][:-1],
                      access_token_secret=api_keys['access_token_secret'][:-1])
    screen_name = user_name
    statuses = api.GetUserTimeline(screen_name=screen_name, count=count)
    tweet_list = [s.text for s in statuses]
    tweet_list1 = [str(r) for r in tweet_list]
    return tweet_list1

# lt = tweet_timeline("realDonaldTrump",3)
# print(lt)

'''
ArvindKejriwal,
realDonaldTrump

'''