"""

Helper.py

Due Date: May 6th, 2020

This is a helper file utilized in the final project to bring in useful methods
to be utilized throughout the program. These are essentially treated as global
functions with limited scope

"""

# Header Variables

__author__      = "Adrian Vasu"
__copyright__   = "Copyright 2020, Adrian Vasu"
__email__       = "vasuad2019@mountunion.edu"
__status__      = "Educational"

# Global Import Statements

import tweepy

# This function creates the twitter authentication object required by tweepy
#   to access the Twitter API and pull the tweets in
def authenticate():
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_secret = ""
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

# This function returns the active twitter handles for the 100 senators from a
#   static file called senators to compare against the list from cspan
def getHandles():
    f = open("wordlists/senators", 'r')

    handles = list()

    for line in f:
        try:
            handles.append(line.split('@', 1)[-1].strip().lower().split(' ')[0])
        except:
            pass

    return handles

# This function builds the party relations between the senators returning a
#   dictionary which has the senator's twitter handle with their affiliated
#   party as the value
def buildPartyRelations():
    f = open("wordlists/senators", 'r')
    relations = dict()
    for line in f:
        try:
            tmp = line.split('@', 1)[-1].strip().lower().split(' ')
            relations[tmp[0]] = tmp[1]
        except:
            pass
    return relations

# This function uses the two files in the repo to build lists of the negative
#   and positive words used to analyze the sentiment in the tweets
def buildWordLists():
    f_neg = open("wordlists/negative-words")
    f_pos = open("wordlists/positive-words")

    negwords = list()
    poswords = list()

    for line in f_neg:
        negwords.append(line.strip().lower())

    for line in f_pos:
        poswords.append(line.strip().lower())

    return negwords, poswords



