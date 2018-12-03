from twitter import Twitter, OAuth

t = Twitter(auth=OAuth(

))

pythonTweets = t.search.tweets(q='#python')