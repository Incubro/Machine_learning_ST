import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'mMdC77ot0w5sU7t7sum9vILpb'
consumer_secret= 'hN2mffBrFSc6K5SiKxaOq2zNlnroiWss7axjcSJQn2l6DBS9bO'

access_token='993531538405912576-Se5gwUO8uc2rYET8izHgDw20KdpKRi4'
access_token_secret='XySbfwwbSg29ZHHfWsS6iOa8142uOs1Nf1DMth2RvCjgx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
print("")
