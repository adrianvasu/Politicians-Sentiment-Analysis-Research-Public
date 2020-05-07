"""

getTweets.py

Due Date: May 6th, 2020

This is a helper file utilized in the final project to retrieve the tweet
information and log it in a CSV file called tweets.csv

"""

# Header Variables

__author__      = "Adrian Vasu"
__copyright__   = "Copyright 2020, Adrian Vasu"
__email__       = "vasuad2019@mountunion.edu"
__status__      = "Educational"

# Global Import Statements

import tweepy
from tweepy import Cursor
import unicodecsv
from unidecode import unidecode
import helper as h

# Worker method to get tweets and populate CSV file
def getTweets(N):
    # Get twitter API authentication object from helper file
    auth = h.authenticate()
    # Create link to twitter API
    api = tweepy.API(auth)

    # open output file
    f = open('csv_files/tweets.csv', 'wb')
    # Create CSV unicode writer
    writer = unicodecsv.writer(f, delimiter = ',', quotechar = '"')
    # Write header row.
    writer.writerow(["twitter_handle",
                    "tweet_id",
                    "tweet_text",
                    "tweet_date",
                    "hashtags"])

    # Loop over the users in the cspan twitter senators list
    for user_obj in Cursor(api.list_members, list_id=4244910).items():

        # Gather info specific to the current user.
        user_info = [user_obj.screen_name.lower()]

        # Get N most recent tweets for the current user.
        for tweet in Cursor(api.user_timeline, screen_name = user_obj.screen_name).items(N):

            # Get info specific to the current tweet of the current user.
            tweet_info = [tweet.id, unidecode(tweet.text).lower(), tweet.created_at]

            # Hashtags are stored as variable-length dictionaries, if present.
            #   Hashtags are not used for this implementation but were going to be used
            #   if the NLP was implemented
            hashtags = []
            hashtags_data = tweet.entities.get('hashtags', None)
            if(hashtags_data != None):
                for i in range(len(hashtags_data)):
                    hashtags.append(unidecode(hashtags_data[i]['text']).lower())

            more_tweet_info = [', '.join(hashtags)]

            # Write data to CSV.
            writer.writerow(user_info + tweet_info + more_tweet_info)

        # Show progress.
        print("Wrote tweets by %s to CSV." % user_obj.screen_name)

    # Close the file
    f.close()
