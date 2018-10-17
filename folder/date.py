from datetime import datetime, timedelta
import re
import io
import csv
import tweepy
from tweepy import OAuthHandler

#Twitter API credentials
consumer_key = "2V8tFuEu8F2eiMbNQFt4pUfFB"
consumer_secret = "n2EkO8cvfXeW8AFdRz9XsrEks3EziLsLlWrsXunp9y5bWSJgkY"
access_key = "831571908013412352-wr7pza2d0b0qgu3W1qZguMzmk8AMIqy"
access_secret = "414kzjo4wHO02jJa3vm37pQy56QSEetqGewM4it5sVNzl"
# create OAuthHandler object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# set access token and secret
auth.set_access_token(access_key, access_secret)
# create tweepy API object to fetch tweets
api = tweepy.API(auth)

now = datetime.today().now()
prev=now-timedelta(days=60)
now=now.strftime("%Y-%m-%d")
prev=prev.strftime("%Y-%m-%d")

target = io.open("try.txt", 'w', encoding='utf-8')
tweets_text = ""

def extract_tweet(hashtag):
	"""csvFile = open('tweets.csv', 'w', newline='', encoding='utf-8')
	csvWriter = csv.writer(csvFile)"""
	try:
		for tweet in tweepy.Cursor(api.search, q=hashtag, since="2018-08-15", until="2018-10-13").items():
			print(tweet)
			if "http" not in tweet.text:
				line = re.sub("[^A-Za-z0-9]", " ", tweet.text)
				print(line)
				tweets_text+line+"\n"
				target.write(line+"\n")
			"""csvWriter.writerow([tweet.text, tweet.created_at])
			csvFile.close()"""
	except:
		return


#hashtag = '#OpMadad OR #KeralaFloods OR #KeralaFloods2018 OR #KeralaFloodRelief OR #KeralaRelief OR #KeralaDonationChallenge'
#print(extract_tweet(hashtag))
