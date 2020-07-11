import tweepy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import textblob
import re

# # # # Twitter Client # # # #
class TwitterClient():

    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticateTwitterApp()
        self.twitter_client = tweepy.API(self.auth)
        self.twitter_user = twitter_user

    def getUserTimelineTweets(self, num_tweets):
        tweets = []
        # gets the tweets of the user and only
        # gets the specified number
        items = tweepy.Cursor(self.twitter_client.user_timeline, id = self.twitter_user).items(num_tweets)
        for tweet in items:
            tweets.append(tweet)

        return tweets

    def getTwitterAPI(self):
        return self.twitter_client

# # # # Twitter Authenticator # # # #
class TwitterAuthenticator():

    def authenticateTwitterApp(self):
        auth = tweepy.OAuthHandler("pjx8stS4d0sxmphKQfsoPVSTs","8zmoJb3eJasIb8LSivuLmr7bSFRxgDUmdVTHDUCc7oThGHTrms")
        auth.set_access_token("300178137-NzvpvKsDBTxo7vSpqBYVricIRZHVU8IPpVTAwjH7","TFhh74d3Wj14zZtcNRSOTcQpaYcIZl9KxyNzYekKXUhTS")
        return auth

# # # # Twitter Streamer # # # #
class TwitterStreamer():
    """
    Class for streaming and processing tweets
    """
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()  

    # this handles connection to the
    #  Twitter Streaming API
    def stream_tweets(self, output_file, hash_tags):
        # create an instance 
        listener = TwitterListener(output_file)

        # create an instance of the authentication
        # and call the get auth method
        auth = self.twitter_authenticator.authenticateTwitterApp()

        # stream the tweets
        stream = tweepy.Stream(auth, listener)

        # Filter the stream with keywords
        stream.filter(track = hash_tags)

# # # # Streaming Data # # # #
class TwitterListener(tweepy.StreamListener):
    """
    Listener class that prints received tweets to stdout
    """
    def __init__(self, output_file):
        self.output_file = output_file

    # Override Methods 
    # takes in the data that is streamed from the StreamListener
    # i.e. listening for tweets
    def on_data(self, data):
        try:
            # print data on console
            print(data)
            # write the data to the output file
            with open(self.output_file, "a") as  f:
                f.write(data)
            return True
        # raise expection if any error occurs
        except BaseException as e:
            print("Error on_data: {}".format(str(e)))
         # to make sure the functin executed correctly
        return True

    # if there is an error it prints the status message
    def on_error(self,status):
        # put check for rates limit (too much data)
        # 420 data so stop connection if occurs
        if status == 420:
            return False
        print(status)

class TweetAnalyser():
    """
    Functionality for analysing and categorising
    content from tweets
    """
    def tweetCleaner(self,tweet):
        return " ".join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\s+)", " ", tweet).split())

    def analyseSentiment(self,tweet):
        analysis = textblob.TextBlob(self.tweetCleaner(tweet))

        # check the polarity of the tweet (sentiment)
        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            return 0
        else:
            return -1

    def tweetsToDataframe(self, tweets):
        df = pd.DataFrame([tweet.text for tweet in tweets],
        columns = ["Tweets"])
        df["date"] = [tweet.created_at for tweet in tweets]
        df["likes"] = [tweet.favorite_count for tweet in tweets]
        df["retweets"] = [tweet.retweet_count for tweet in tweets]
        return df

if __name__ ==  "__main__":
    
    # instantiate twitter client
    twitter_client = TwitterClient()
    api = twitter_client.getTwitterAPI()
    tweet_analyser = TweetAnalyser()

    # Stream tweets
    tweets = api.user_timeline(screen_name = "realDonaldTrump", count = 2000)
    # print(dir(tweets[0])) gives you all the info you can access from a tweet

    # create dataframe
    df = tweet_analyser.tweetsToDataframe(tweets)
    #print(df.head(10))

    # Time Series Analysis
    """    
    ts_likes = pd.Series(df["likes"].values, index = df["date"])
    ts_likes.plot(figsize=(16,4), color = "r")
    plt.show()
    """

    ## Correlation Analysis
    """
    ts_likes = pd.Series(df["likes"].values, index = df["date"])
    ts_likes.plot(figsize=(16,4), label = "likes", legend = True)

    ts_retweets = pd.Series(df["retweets"].values, index = df["date"])
    ts_retweets.plot(figsize=(16,4), label = "retweets", legend = True)
    plt.show()
    """

    df["sentiment"] = [tweet_analyser.analyseSentiment(tweet) for tweet in df["Tweets"]]
    print(df.head(10))

    # TODO investigate corr between likes/retweets and pos/neg words


    #hash_tags = ["donald trump", "America"]
    #output_file = "tweets.json"
    #twitter_client = TwitterClient()
    #print(twitter_client.getUserTimelineTweets(5))
    #twit_streamer = TwitterStreamer()
    #twit_streamer.stream_tweets(output_file, hash_tags)
