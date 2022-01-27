
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import json

consumer_key = "ASRAGdCJdtmQ5bLWGBGZYd0oy"
consumer_key_secret = "x4zA9z6FOCwKtFVGRK3dtEZDuxyeQrNvTRzVSI4g83WFe4jirT"
access_token = "1368632915031040002-L98lPEecMSwK1J824JPDLN068VuafH"
access_token_secret = "zFg8F5hIIGmApVu52u8jkFIF7MseamgdiX7ZjCXIDWplI"

class StdoutListener(StreamListener):
    def on_data(self,data):
        try:
            data = json.loads(data)
            tweet = data['xlhome']
            with open('tweet.csv', 'a', encoding='utf-8') as f:
                saveFile = open('gabung.csv','a')
                f.write(tweet)
                f.write('\n')
                f.close()
            return True
        except BaseException as e:
            print('Failed'(e))
        
        def on_error(self_status):
            print(status)

#streaming
l = StdoutListener()
auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
stream = Stream(auth,l)
stream.filter(track=['xlhome'])
