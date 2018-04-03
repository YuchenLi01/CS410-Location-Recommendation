#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 11:43:10 2018

@author: liyuchen
"""

# libraries
import codecs
import pickle
import operator

# codes
import search

'''
Read the pickle file.
'''
def read_pickle(fn):
    with codecs.open(fn, 'rb') as f:
        t = pickle.load(f, encoding='latin1')
    return t

'''
Return a list of Tweet objects from a query.
The relevance measure is a simple one, using inverted index (without BM25)
input:
    q: query string
    id_to_tweet_dict: a dictionary (tweetID -> Tweet object)
    num_res: the max number of resulting tweets needed (default 3)
output:
    relevant_tweets: a list of Tweet objects (now more than num_res), sorted by relevance (high->low)
'''
def query_to_tweets_plain(q, id_to_tweet_dict, num_res=3):
    q_words = q.split()
    
    # score: dictionary (tweetID -> relevance score)
    score = {}
    for w in q_words:
        res = search.search(w)
        for tweetID in res.postings.keys():
            count_in_tweet = res.postings[tweetID]
            if (tweetID not in score.keys()):
                score[tweetID] = count_in_tweet
            else:
                score[tweetID] += count_in_tweet
    
    relevant_tweets = []
    for i in range(num_res):
        if (len(score) >= 1):
            tweetID = max(score.items(), key=operator.itemgetter(1))[0]
            tweet = id_to_tweet_dict[tweetID]
            relevant_tweets.append(tweet)
            del score[tweetID] 
    return relevant_tweets



'''
Main
'''
if __name__=="__main__":
    
    res = search.search('good')
    res.print_result()