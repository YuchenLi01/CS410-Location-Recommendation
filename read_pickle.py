#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import codecs
import pickle
#from learner import search

'''
Read the pickle file containing the processed tweets data.
Output a list of tweets object.
'''
def read_pickle(fn):
    with codecs.open(fn, 'rb') as f:
        t = pickle.load(f, encoding='latin1')
    return t
    

if __name__=="__main__":
    
    # example
    # read the pickle file containing the processed tweets data.
    # t is a list of tweets object.
    '''
    fn = 'data/tweets1100000_tokenized_group/tweets1100000_tokenized_0.pickle'
    t = read_pickle(fn)
    '''
    
    # read inverted index # see search.py
    '''
    fn = 'learner/data/tweets1100000_partial_0_.pickle'
    t = search.read_pickle(fn)
    '''
    
    '''
    2018.3.22
    Create id_to_tweet_dict: a dictionary (tweetID -> Tweet object)
    '''
    #fn = 'data/tweets1100000_tokenized.pickle'
    #t = read_pickle(fn)
    
    id_to_tweet_dict = {}
     
    