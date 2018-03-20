import json

class TweetBackend:
	def __init__(self, user, text, time, lat, lng):
		self.user = user
		self.text = text
		self.time = time
		self.lat = lat
		self.lng = lng

    # {
    #   user: 'username1',
    #   text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus fringilla egestas quam, vitae molestie ex pharetra et.',
    #   time: 'Feb 23 12:24',
    #   lat: 34.074182,
    #   lng: -118.292773
    # }

	def to_json_string(self):
		dic = {
			"user": self.user,
			"text": self.text,
			"time": self.time,
			"lat": self.lat,
			"lng": self.lng
		}
		return json.dumps(dic)
