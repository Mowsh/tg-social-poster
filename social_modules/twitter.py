import tweepy
import os
from social_modules.social_interface import SocialModuleInterface

tweepy_consumer_key = os.environ.get('X_CONSUMER_KEY')
tweepy_consumer_secret = os.environ.get('X_CONSUMER_SECRET')
tweepy_bearer_token = os.environ.get('X_BEARER_TOKEN')
tweepy_access_token = os.environ.get('X_ACCESS_TOKEN')
tweepy_access_token_secret = os.environ.get('X_ACCESS_TOKEN_SECRET')

class TwitterModule(SocialModuleInterface):
    async def post(self, text, photo, filename):
        try:
            auth = tweepy.OAuthHandler(tweepy_consumer_key, tweepy_consumer_secret)
            auth.set_access_token(tweepy_access_token, tweepy_access_token_secret)
            api = tweepy.API(auth)

            client = tweepy.Client(bearer_token=tweepy_bearer_token,
                    access_token=tweepy_access_token,
                    access_token_secret=tweepy_access_token_secret,
                    consumer_key=tweepy_consumer_key,
                    consumer_secret=tweepy_consumer_secret)

            media_ids = None
            if photo is not None:
                media = api.media_upload(filename=filename, file=photo)
                media_ids = [media.media_id]
            
            client.create_tweet(text=text, media_ids=media_ids)
        except Exception as error:
            print("Twitter error", error)
            