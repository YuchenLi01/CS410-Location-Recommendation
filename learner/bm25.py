import pickle
import codecs
import math

INVERT_IDX_FN = 'data/tweets1100000_inverted_index.pickle'
CORPUS_FN = 'data/tweets1100000.txt'
M = 1000000.0
K = 1.2
B = 0.75

class Tweet:
    def __init__(self, cur_line, cur_id, tknzr = None):
       items = cur_line.split('\x01')

       self.id = cur_id
       self.lat = float(items[2])
       self.lng = float(items[3])
       self.datetime = items[4]
       self.text = ' '.join(items[6].split('\t')) # the text is preprocessed in someway
       self.raw = items[7] # raw tweet

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

class BM25:
	def __init__(self):
		invert_idx_dump = pickle.load(codecs.open(INVERT_IDX_FN, 'rb'), encoding='latin1')
		self.word2id = invert_idx_dump[0]
		self.id2invert_idx = invert_idx_dump[1]

	def query(self, keywords):
		candidate_dic = {}
		for cur_word in keywords:
			if (cur_word not in self.word2id) or (not self.id2invert_idx[self.word2id[cur_word]].postings):
				continue
			invert_idx_obj = self.id2invert_idx[self.word2id[cur_word]]
			for doc_id in list(invert_idx_obj.postings.keys())[:10]:
				candidate_dic[doc_id] = candidate_dic.get(doc_id, 0) + self.get_score(invert_idx_obj, doc_id)
		print(candidate_dic)

	def get_score(self, invert_idx_obj, doc_id):
		cnt = invert_idx_obj.postings[doc_id]
		idf = self.get_idf(invert_idx_obj)
		tf = self.get_tf(doc_id)
		return idf * ((K + 1.0) * cnt) / (cnt + K * tf)

	def get_tf(self, doc_id):
		return 1 - B + B # 1 - b + b * doc_len / avg_len

	def get_idf(self, invert_idx_obj):
		return math.log((M + 1.0) / invert_idx_obj.doc_freq)


def load():
	words = []
	fn = 'data/tweets1100000_inverted_index.pickle'
	t = pickle.load(codecs.open(fn, 'rb'), encoding='latin1')
	obj = t[0]['traffic']
	print(t[1][obj].postings)

def main():
	bm25_obj = BM25()
	print("Querying")
	bm25_obj.query(["food", "traffic"])

	fn = 'data/tweets1100000_tokenized_0.pickle'
	with codecs.open(fn, 'rb') as f:
		tweets = pickle.load(f, encoding = 'latin1') #1/20 of all pickles
		print(tweets[0])

if __name__ == "__main__":
  main()
