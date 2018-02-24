FILE_NAME = "./data/tweets1100000.txt"
TWEET_NUM = 10

class Tweet:
	def __init__(self, cur_line, cur_id):
		items = cur_line.split('\x01')
		self.id = cur_id
		self.lat = float(items[2])
		self.lng = float(items[3])
		self.datetime = items[4]
		self.text = ' '.join(items[6].split('\t')) # the text is preprocessed in someway
		self.raw = items[7] # raw tweet
		# self.words = self.text.split(' ') # I think we should better preprocess the tweets ourselfs

def main():
	tweets = []
	with open(FILE_NAME, 'r') as cur_file:
		cur_id = 0
		for cur_line in cur_file:
			cur_tweet = Tweet(cur_line, cur_id)
			tweets.append(cur_tweet)
			cur_id += 1
			if cur_id == TWEET_NUM:
				break

if __name__ == "__main__":
	main()