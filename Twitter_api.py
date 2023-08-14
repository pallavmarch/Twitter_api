#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
get_ipython().system('pip install tweepy')
import tweepy as tw


# In[9]:


consumer_api_key = '1536368328750809088-ekmfDXge1reU3A3ou9bX0zYOOncPVA'
consumer_api_secret = 'DMqjxsA6aAyP6uVFIPxFaetBz0rghbFS8WROTUOVk6NTp'


# In[13]:


auth = tw.OAuthHandler(consumer_api_key, consumer_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)


# # Tweets

# In[14]:


search_words = "#Tiktok -filter:retweets" 
date_since = "2023-01-31"
date_until="2023-08-12"


# In[26]:


tweets = tw.Cursor(api.search_tweets,
                  q=search_words,
                  lang="en",
                  since=date_since,
                  until=date_until
                  ).items(1500)


# # Tweets retrival

# In[27]:


twee=[]


# In[28]:


from tqdm import tqdm


# In[30]:


for i in tqdm(tweets):
    twee.append(i)


# In[ ]:


twee_df = pd.DataFrame()
for i in tqdm(twee):
    hashtags = []
    #try:
    #    for hashtag in tweet.entities["hashtags"]:
    #        hashtags.append(hashtag["text"])
    #except:
    #    pass
    tweets_df = tweets_df.append(pd.DataFrame({'user_name': tweet.user.name, 
                                               'user_location': tweet.user.location,\
                                               'user_description': tweet.user.description,
                                               'user_created': tweet.user.created_at,
                                               'user_followers': tweet.user.followers_count,
                                               'user_friends': tweet.user.friends_count,
                                               'user_favourites': tweet.user.favourites_count,
                                               'user_verified': tweet.user.verified,
                                               'date': tweet.created_at,
                                               'text': tweet.text, 
                                               'hashtags': [hashtags if hashtags else None],
                                               'source': tweet.source,
                                               'is_retweet': tweet.retweeted}, index=[0]))


# In[ ]:


tweets_df

