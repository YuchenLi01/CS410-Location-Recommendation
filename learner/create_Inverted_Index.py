FILE_NAME = "./data/tweets1100000.txt"
TWEET_NUM = 1200000
import pickle
import codecs
#from nltk.tokenize import TweetTokenizer
class Tweet:
    def __init__(self, cur_line, cur_id, tknzr = None):
       items = cur_line.split('\x01')

       self.id = cur_id
       self.lat = float(items[2])
       self.lng = float(items[3])
       self.datetime = items[4]
       self.text = ' '.join(items[6].split('\t')) # the text is preprocessed in someway
       self.raw = items[7] # raw tweet
        # self.words = self.text.split(' ') # I think we should better preprocess the tweets ourselfs
       #self.word_tokens = None # tokens returned from nltk.tokenize.TweetTokenizer from raw text
       #if (tknzr != None):
       #    self.word_tokens = tknzr.tokenize(self.raw)
		#self.raw = items[7] # raw tweet
		# self.words = self.text.split(' ') # I think we should better preprocess the tweets ourselfs
class inverted_idx_obj:
    def __init__(self):

        self.doc_freq = 0
        self.total_freq = 0
        self.postings = {}

    def update(self, DOC_ID):
        if DOC_ID not in self.postings.keys():
            self.postings[DOC_ID] = 0
            self.doc_freq += 1
        self.postings[DOC_ID] += 1
        self.total_freq += 1




def create_inverted_index():
    #tknzr = TweetTokenizer(preserve_case=False, reduce_len=True, strip_handles=True)
    #cur_id = 0 #doc (tweet) ID
    ID = 0 # term ID
    part_inverted_index_dict = {}
    term_ID_dict = {}

    for num in range(0, 20):
        fn = 'data/tweets1100000_tokenized_' + str(num) + '.pickle'
        with codecs.open(fn, 'rb') as f:
            tweets = pickle.load(f, encoding = 'latin1') #1/20 of all pickles
            for cur_line in tweets:

            #with open(FILE_NAME, 'r', encoding = 'UTF-8') as cur_file:

            #loop = 0
                for term in cur_line.text.split():
                #print(cur_id)
                #if len(cur_line.split('\x01')) >=8:

                #cur_tweet = Tweet(cur_line, cur_id)
                    #print(term)
                    #print(ID)
                    term = term.lower()
                    if not(term in term_ID_dict.keys()):
                        term_ID_dict[term] = ID
                        part_inverted_index_dict[ID] = inverted_idx_obj()
                        part_inverted_index_dict[ID].update(cur_line.id)
                        ID += 1
                    else:
                        part_inverted_index_dict[term_ID_dict[term]].update(cur_line.id)

            tweets.clear()

            #if cur_id == TWEET_NUM* (loop + 1) - 1:
                #dump the two dicts

    s = sorted(part_inverted_index_dict.items(), key = lambda item: item[1].doc_freq, reverse = True)
    part_inverted_index_dict.clear()
    cnt = 0
    for k, v in s:
        part_inverted_index_dict[k] = v
        cnt += 1
        if cnt >=10000:
            break

    out_fn = 'data/tweets1100000_inverted_index.pickle'
    with codecs.open(out_fn, 'wb') as g:
        #pickle.dump(term_ID_ dict, f)
        #pickle.dump(part_inverted_index_dict, f)
        ls = [term_ID_dict, part_inverted_index_dict]
        pickle.dump(ls, g)

        #loop += 1
        #print(loop)

    #print(cur_id)
        #print(cur_id+1)
    part_inverted_index_dict.clear()
    term_ID_dict.clear()
    ls.clear()
    #out_fn = './data/tweets1100000_partial_'+str(loop)+'_.pickle'
    '''with codecs.open(out_fn, 'wb') as f:
        ls = [term_ID_dict, part_inverted_index_dict]
        pickle.dump(ls, f)
    '''






if __name__ == "__main__":
	create_inverted_index()
