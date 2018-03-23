# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 05:17:29 2018

@author: lenovo
"""
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
    
class search_result:
    def __init__(self, term):
        self.term = term
        
        self.doc_freq = 0
        self.total_freq = 0
        self.postings = {}
    def update(self, num_of_doc_freq, num_of_total_freq, new_postings):
        self.doc_freq += num_of_doc_freq
        self.total_freq += num_of_total_freq
        for i in new_postings.keys():
            if i not in self.postings.keys():
                self.postings[i] = new_postings[i]
    def print_result(self):
        #print(str(self.term) + ":")
        print("Document frequency: %d" % self.doc_freq )
        print("Total frequency: %d" % self.total_freq )
        
        #for i in self.postings.keys():
            #print("%s exists at Tweet No. %d %d times" %(self.term, i, self.postings[i]))
        
def search(kw):
    kw = kw.lower()
    result = search_result(kw)
    
    fn = 'data/tweets1100000_inverted_index.pickle'
        
    with codecs.open(fn, 'rb') as f:
        t = pickle.load(f, encoding='latin1')
        #search the kw within the current loop, including the 
        #doc_freq, total_freq, and all postings. Add/append them together.
        #if not exist in the current loop, continue to the next loop
        if kw in t[0].keys():
            term_id = t[0][kw]
            print('term_id: %d' % term_id)
            if term_id in t[1].keys():
                result.update(t[1][term_id].doc_freq, t[1][term_id].total_freq, t[1][term_id].postings)    
            #print(len(t[1][term_id].postings))
        '''print(t[1][term_id].doc_freq)
        print(t[1][term_id].total_freq)
        print(t[1][term_id].postings)
        '''
            
        t = None
        
    return result


if __name__ == "__main__":
    result = search('hell')
    result.print_result()
    #result.doc_freq = 0, the document frequency, int
    #result.total_freq = 0, the total frequency, int
    #result.postings = {}, the dictionary with documents as keys and the frequency in that document as value {doc_ID(int): freq(int)}
    #use tokenized word instead of the original, only keep first 10000. 
