from datetime import datetime, timedelta
import re
import io
import csv
import tweepy
from tweepy import OAuthHandler

#Twitter API credentials
'''
consumer_key = "2V8tFuEu8F2eiMbNQFt4pUfFB"
consumer_secret = "n2EkO8cvfXeW8AFdRz9XsrEks3EziLsLlWrsXunp9y5bWSJgkY"
access_key = "831571908013412352-wr7pza2d0b0qgu3W1qZguMzmk8AMIqy"
access_secret = "414kzjo4wHO02jJa3vm37pQy56QSEetqGewM4it5sVNzl"
'''
consumer_key = 'sz6x0nvL0ls9wacR64MZu23z4'
consumer_secret = 'ofeGnzduikcHX6iaQMqBCIJ666m6nXAQACIAXMJaFhmC6rjRmT'
access_key = '854004678127910913-PUPfQYxIjpBWjXOgE25kys8kmDJdY0G'
access_secret = 'BC2TxbhKXkdkZ91DXofF7GX8p2JNfbpHqhshW1bwQkgxN'

# create OAuthHandler object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# set access token and secret
auth.set_access_token(access_key, access_secret)
# create tweepy API object to fetch tweets
api = tweepy.API(auth)



now = datetime.today().now()
prev=now-timedelta(days=87)
end=now-timedelta(days=57)
now=now.strftime("%Y-%m-%d")
end=end.strftime("%Y-%m-%d")

target1 = io.open("day1.txt", 'w', encoding='utf-8')
target2 = io.open("day2.txt", 'w', encoding='utf-8')
target3 = io.open("day3.txt", 'w', encoding='utf-8')
target4 = io.open("day4.txt", 'w', encoding='utf-8')
target5 = io.open("day5.txt", 'w', encoding='utf-8')
target6 = io.open("day6.txt", 'w', encoding='utf-8')
tweets_text = ""
#start_date = datetime.datetime(2018, 8, 15, 12, 00, 00)
#end_date = datetime.datetime(2018, 9, 15, 12, 00, 00)
def extract_tweet(hashtag):

	
	for tweet in tweepy.Cursor(api.user_timeline, screen_name='FloodsUpdate', lang = "en", since = "2018-08-18" , until = "2018-08-25").items():#, until=end).items():
		#print(tweet.created_at.date()='2018-08-15')
		#print(tweet.created_at.date())
		#if "http" not in tweet.text:
		if str(tweet.created_at.date())=='2018-08-18':
			print('hello')
			line = re.sub("[^A-Za-z0-9]", " ", tweet.text)
			#print(line)
			tweets_text+line+"\n"
			target1.write(line+"\n")
		if str(tweet.created_at.date())=='2018-08-19':
			line = re.sub("[^A-Za-z0-9]", " ", tweet.text)
			#print(line)
			tweets_text+line+"\n"
			target2.write(line+"\n")
		if str(tweet.created_at.date())=='2018-08-20':
			line = re.sub("[^A-Za-z0-9]", " ", tweet.text)
			#print(line)
			tweets_text+line+"\n"
			target3.write(line+"\n")
		if str(tweet.created_at.date())=='2018-08-21':
			line = re.sub("[^A-Za-z0-9]", " ", tweet.text)
			#print(line)
			tweets_text+line+"\n"
			target4.write(line+"\n")
		if str(tweet.created_at.date())=='2018-08-22':
			line = re.sub("[^A-Za-z0-9]", " ", tweet.text)
			#print(line)
			tweets_text+line+"\n"
			target5.write(line+"\n")
		if str(tweet.created_at.date())=='2018-08-25':
			line = re.sub("[^A-Za-z0-9]", " ", tweet.text)
			#print(line)
			tweets_text+line+"\n"
			target6.write(line+"\n")



hashtag = '#OpMadad OR #KeralaFloods OR #KeralaFloods2018 OR #KeralaFloodRelief OR #KeralaRelief OR #KeralaDonationChallenge'
print(extract_tweet(hashtag))
