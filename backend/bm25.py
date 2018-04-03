import pickle
import codecs
import math

INVERT_IDX_FN = 'data/tweets1100000_inverted_index.pickle'
CORPUS_FN = 'data/tweets1100000.txt'
NUM_PICKLE = 2
M = 1000000.0
K = 1.2
B = 0.75
MAX_DOC_NUM = 10
AVG_LEN = 27

class Tweet:
    def __init__(self, cur_line, cur_id, tknzr = None):
       items = cur_line.split('\x01')
       self.id = cur_id
       self.lat = float(items[2])
       self.lng = float(items[3])
       self.datetime = items[4]
       self.text = ' '.join(items[6].split('\t')) # the text is preprocessed in someway
       self.raw = items[7] # raw tweet

class NewTweet:
	def __init__(self, old_tweet):
		# self.length = len(old_tweet.raw.split(' '))
		self.id = old_tweet.id
		self.doc_len_norm = 1 - B + B * len(old_tweet.raw.split(' ')) / AVG_LEN
		time_arr = old_tweet.datetime.split(' ')
		tmp = time_arr[3].split(':')
		self.user = "User-{}".format(self.id)
		self.text = old_tweet.raw
		self.time = "{} {} {}:{}".format(time_arr[1], time_arr[2], tmp[0], tmp[1])
		self.lat = float(old_tweet.lat)
		self.lng = float(old_tweet.lng)

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

class Corpus:
	def __init__(self):
		self.id2tweet = {}
		# l = 0
		for num in range(0, NUM_PICKLE):
			fn = 'data/tweets1100000_tokenized_group/tweets1100000_tokenized_' + str(num) + '.pickle'
			with codecs.open(fn, 'rb') as f:
				tweets = pickle.load(f, encoding = 'latin1') #1/20 of all pickles
				for cur_tweet in tweets:
					self.id2tweet[cur_tweet.id] = NewTweet(cur_tweet)
		# 			l += self.id2tweet[cur_tweet.id].length
		# print(l / len(self.id2tweet))

class BM25:
	def __init__(self):
		invert_idx_dump = pickle.load(codecs.open(INVERT_IDX_FN, 'rb'), encoding='latin1')
		self.word2id = invert_idx_dump[0]
		self.id2invert_idx = invert_idx_dump[1]
		print("Reading corpus")
		self.id2tweet = Corpus().id2tweet
		print("Reading corpus done")

	def query(self, keywords):
		candidate_dic = {}
		for cur_word in keywords:
			if (cur_word not in self.word2id) or (self.word2id[cur_word] not in self.id2invert_idx):
				continue
			invert_idx_obj = self.id2invert_idx[self.word2id[cur_word]]
			doc_cnt = 0
			for doc_id in list(invert_idx_obj.postings.keys()):
				if doc_id not in self.id2tweet:
					continue
				candidate_dic[doc_id] = candidate_dic.get(doc_id, 0) + self.get_score(invert_idx_obj, doc_id)
				doc_cnt += 1
				if doc_cnt == MAX_DOC_NUM:
					break
		doc_id_score_arr = list(map(lambda x : (x, candidate_dic[x]), candidate_dic))
		doc_id_score_arr = sorted(doc_id_score_arr, key=lambda x : -x[1])
		doc_id_arr = list(map(lambda x : x[0], doc_id_score_arr))
		tweet_arr = list(map(lambda x : self.id2tweet[x], doc_id_arr))
		for t in tweet_arr:
			print(t.text)

	def get_score(self, invert_idx_obj, doc_id):
		cnt = invert_idx_obj.postings[doc_id]
		idf = self.get_idf(invert_idx_obj)
		doc_len_norm = self.id2tweet[doc_id].doc_len_norm
		return idf * ((K + 1.0) * cnt) / (cnt + K * doc_len_norm)

	def get_idf(self, invert_idx_obj):
		return math.log((M + 1.0) / invert_idx_obj.doc_freq)

def main():
	bm25_obj = BM25()
	bm25_obj.query(["drink", "beer"])

if __name__ == "__main__":
  main()
