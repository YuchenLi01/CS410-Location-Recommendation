from flask import Flask, request, jsonify
from tweet_backend import TweetBackend
import json

app = Flask(__name__)

fake_tweet1 = TweetBackend(
	"username1",
	"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus fringilla egestas quam, vitae molestie ex pharetra et.",
	"Feb 23 12:24",
	34.074182,
	-118.292773
)

fake_tweet2 = TweetBackend(
	"username2",
	"In ac tellus ac nisl placerat pharetra. Proin elementum tortor erat, tincidunt congue quam mattis ut. Sed sollicitudin vestibulum quam, id viverra purus congue sit amet. Suspendisse iaculis elit non tortor fermentum porttitor.",
	"Feb 25 21:32",
	34.0522342,
	-118.2436849
)

fake_heatmap = [
	[34.0522342, -118.2436849],
	[34.0522342, -118.2436849],
	[34.0522342, -118.2436849],
]

def get_tweets(query_words):
	res_arr = [fake_tweet1, fake_tweet2]
	res_arr = list(map(lambda x : x.to_json_string(), res_arr))
	return res_arr

def get_heatmap(query_words):
	return fake_heatmap

@app.route("/")
def serving():
	query_obj = request.args.get('words')
	query_obj = json.loads(query_obj)
	tweet_results = get_tweets(query_obj["words"])
	heatmap_results = get_heatmap(query_obj["words"])
	res = {}
	res["tweets"] = tweet_results
	res["heatmap"] = heatmap_results
	res = jsonify(res)
	res.headers['Access-Control-Allow-Origin'] = '*'
	res.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE, OPTIONS'
	return res

if __name__ == '__main__':
  app.run(debug=True)
