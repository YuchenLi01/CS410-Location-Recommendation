#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import codecs
import pickle

'''
Read the pickle file containing the processed tweets data.
Output a list of tweets object.
'''
def read_pickle(fn):
    with codecs.open(fn, 'rb') as f:
        t = pickle.load(f, encoding='latin1')
    return t
    

if __name__=="__main__":
    
    # read the pickle file containing the processed tweets data.
    # t is a list of tweets object.
    fn = 'data/tweets1100000_tokenized.pickle'
    t = read_pickle(fn)
