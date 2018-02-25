import codecs
from nltk.tokenize import TweetTokenizer
import pickle

TWEET_NUM = 10
FILE_NAME = "./data/tweets1100000.txt"

'''
A Tweet object contains the information of a single tweet
'''
class Tweet:
    def __init__(self, cur_line, cur_id, tknzr=None):
        items = cur_line.split('\x01')
        self.id = cur_id
        self.lat = float(items[2]) # latitude
        self.lng = float(items[3]) # longitude 
        self.datetime = items[4]
        self.useful_words = items[6].split('\t') # a list of lower case words, with stop words removed
        self.text = ' '.join(self.useful_words) # the text is preprocessed in someway, with stop words removed
        self.raw = items[7] # raw tweet
        # self.words = self.text.split(' ') # I think we should better preprocess the tweets ourselfs
        self.word_tokens = None # tokens returned from nltk.tokenize.TweetTokenizer from raw text
        if (tknzr != None):
            self.word_tokens = tknzr.tokenize(self.raw)

def read_tweets(file_name):
    tweets = []
    tknzr = TweetTokenizer(preserve_case=False, reduce_len=True, strip_handles=True)
    with codecs.open(file_name, 'r') as cur_file:
        cur_id = 0
        for cur_line in cur_file:
            try:
                #print('cur_line == ', cur_line) #debug
                #print('cur_id == ', cur_id) #debug
                cur_tweet = Tweet(cur_line, cur_id, tknzr)
                tweets.append(cur_tweet)
            except: # this happens frequently
                #print('cur_line == ', cur_line)
                #print('exceptions while reading cur_id == ', cur_id)
                #break
                pass
            #if cur_id == TWEET_NUM: #debug
            #    break #debug
            cur_id += 1
    return tweets
        

'''
Main
'''
if __name__=="__main__":
    
    # read in the tweet data
    tweets = read_tweets(FILE_NAME)
    
    # dump the processed data
    out_fn = 'data/tweets1100000_tokenized.pickle'
    with codecs.open(out_fn, 'wb') as f:
        pickle.dump(tweets, f)