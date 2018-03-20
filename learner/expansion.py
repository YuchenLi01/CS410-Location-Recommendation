import pickle
import codecs
import gensim
import numpy as np
import scipy.spatial

class Tweet:
  def __init__(self, cur_line, cur_id):
   items = cur_line.split('\x01')

   self.id = cur_id
   self.lat = float(items[2])
   self.lng = float(items[3])
   self.datetime = items[4]
   self.text = ' '.join(items[6].split('\t')) # the text is preprocessed in someway

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

def dump_top_2000_words():
		words = []
		fn = 'data/tweets1100000_partial_0_.pickle'
		t = pickle.load(codecs.open(fn, 'rb'), encoding='latin1')
		for w in list(t[0].keys()):
			term_id = t[0][w]
			if term_id in t[1].keys():
				freq = t[1][term_id].doc_freq
				words.append((w, freq))
		fn2 = 'data/top2000words.pickle'
		words = sorted(words, key=lambda x : -x[1])[:2000]
		words = list(map(lambda x : x[0], words))
		pickle.dump(words, codecs.open(fn2, 'wb'))

def dump_top_2000_vecs():
		fn = 'data/top2000words.pickle'
		words = pickle.load(codecs.open(fn, 'rb'))
		vecs = {}
		model = gensim.models.KeyedVectors.load_word2vec_format('./data/GoogleNews-vectors-negative300.bin', binary=True)
		for word in words:
			try:
				vec = model.wv[word]
				vecs[word] = vec
			except:
				continue
		fn2 = 'data/top2000wordsvecs.pickle'
		pickle.dump(vecs, codecs.open(fn2, 'wb'))

def dump_top_2000_expansion():
	fn = 'data/top2000wordsvecs.pickle'
	vecs = pickle.load(codecs.open(fn, 'rb'))
	words = vecs.keys()
	res = {}
	i = 0
	for wi in words:
		if wi not in vecs:
			continue
		vi = vecs[wi]
		dists = []
		for wj in words:
			if wj == wi or wj not in vecs:
				continue
			vj = vecs[wj]
			dist = scipy.spatial.distance.cosine(vi, vj)
			dists.append((wj, dist))
		expanded = sorted(dists, key=lambda x : x[1])[:5]
		expanded = list(map(lambda x : x[0], expanded))
		if len(expanded) > 0:
			res[wi] = expanded
		i += 1
		if i % 100 == 0:
			print(i)
	fn2 = 'data/top2000wordsexpansion.pickle'
	pickle.dump(res, codecs.open(fn2, 'wb'))

def main():
	fn = 'data/top2000wordsexpansion.pickle'
	expansion = pickle.load(codecs.open(fn, 'rb'))
	print(expansion['beer'], expansion['good'])

if __name__ == "__main__":
	main()
