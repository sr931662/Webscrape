import json
import time

import pandas as pd
from tqdm.notebook import tqdm
import snscrape.modules.twitter as sntwitter
import snscrape.modules.reddit as red

rquery = input('Enter your query here : ')
rlim =input('Enter the limit : ')
Reddit = []
for redt in red.RedditSearchScraper(rquery).get_items():
    # print(redt.body)
    if len(Reddit) == rlim:
            break
    else:
        Reddit.append([redt.id, redt.author, redt.date, redt.body])
        # Reddit.append(redt.title)

        # print(Reddit)
        # time.sleep

redf = pd.DataFrame(Reddit, columns=['Redditer ID', 'Redditer', 'Date', 'Title'])

redf.to_csv('Reddit_csv.csv', index=False)
rejf = pd.read_csv('Reddit_csv.csv')
rejf.to_json('Reddit_json.json')

# print(redf)

# # # # # # # FOR TWITTER # # # # # # # # #
# query = input("Enter the word to search : ")
# tweets = []
# print('max 1000000/day only!!')
# tlim = input('\nEnter limit : ')
# for tweet in sntwitter.TwitterSearchScraper(query).get_items():
#     # print(vars(tweet))
#     # break
#     if len(tweets) == tlim:
#         break
#     else:
#         tweets.append([tweet.date, tweet.user.username, tweet.rawContent])
#         # print(tweet.user.username)
#
# df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
# df.to_csv('tweet_csv.csv')
# csv = pd.read_csv('tweet_csv.csv')
# csv.to_json('tweet_json.json')
# print(pd.read_json('tweet_json.json'))

