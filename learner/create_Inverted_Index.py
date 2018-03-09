FILE_NAME = "./data/tweets1100000.txt"
TWEET_NUM = 60000
import pickle
import codecs
class Tweet:
    def __init__(self, cur_line, cur_id):
       items = cur_line.split('\x01')
        
       self.id = cur_id
       self.lat = float(items[2])
       self.lng = float(items[3])
       self.datetime = items[4]
       self.text = ' '.join(items[6].split('\t')) # the text is preprocessed in someway
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
    with open(FILE_NAME, 'r', encoding = 'UTF-8') as cur_file:
        cur_id = 0
        loop = 0
        ID = 0
        part_inverted_index_dict = {}  
        term_ID_dict = {} 
        for cur_line in cur_file:
        
            #print(cur_id)
               
            
            if len(cur_line.split('\x01')) >=8:
                
                cur_tweet = Tweet(cur_line, cur_id)
                for term in cur_tweet.text.split():
                
                    if not(term in term_ID_dict.keys()):
                        term_ID_dict[term] = ID                   
                        part_inverted_index_dict[ID] = inverted_idx_obj()
                        part_inverted_index_dict[ID].update(cur_id)
                        ID += 1
                    else:
                        part_inverted_index_dict[term_ID_dict[term]].update(cur_id)
                cur_id += 1
            else:
                cur_id += 1
            if cur_id == TWEET_NUM* (loop + 1) - 1:
                #dump the two dicts
                out_fn = 'data/tweets1100000_partial_'+str(loop)+'_.pickle'
                with codecs.open(out_fn, 'wb') as f:
                    #pickle.dump(term_ID_dict, f)
                    #pickle.dump(part_inverted_index_dict, f)
                    ls = [term_ID_dict, part_inverted_index_dict]
                    pickle.dump(ls, f)
                    
                loop += 1
                print(loop)
                #print(cur_id+1)
                part_inverted_index_dict.clear() 
                term_ID_dict.clear()
                ls.clear()
        out_fn = 'data/tweets1100000_partial_'+'last_loop'+'_.pickle'
        with codecs.open(out_fn, 'wb') as f:
            ls = [term_ID_dict, part_inverted_index_dict]
            pickle.dump(ls, f)
         
        
        
        



if __name__ == "__main__":
	create_inverted_index()