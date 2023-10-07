import json
import os
import tweepy

tg_api_key = os.environ.get('TG_API_KEY')
channel_id = int(os.environ.get('CHANNEL_ID'))

tweepy_consumer_key = os.environ.get('X_CONSUMER_KEY')
tweepy_consumer_secret = os.environ.get('X_CONSUMER_SECRET')
tweepy_bearer_token = os.environ.get('X_BEARER_TOKEN')
tweepy_access_token = os.environ.get('X_ACCESS_TOKEN')
tweepy_access_token_secret = os.environ.get('X_ACCESS_TOKEN_SECRET')

def lambda_handler(event, context):
    tg_event = json.loads(event['body'])
    print(tg_event)
    
    if 'channel_post' in tg_event and tg_event['channel_post']['chat']['id'] == channel_id:
        message_text = tg_event['channel_post']['text'] if 'text' in tg_event['channel_post'] else ""
        
        auth = tweepy.OAuthHandler(tweepy_consumer_key, tweepy_consumer_secret)
        auth.set_access_token(tweepy_access_token, tweepy_access_token_secret)

        # api = tweepy.API(auth)
        client = tweepy.Client(bearer_token=tweepy_bearer_token,
                access_token=tweepy_access_token,
                access_token_secret=tweepy_access_token_secret,
                consumer_key=tweepy_consumer_key,
                consumer_secret=tweepy_consumer_secret)

        client.create_tweet(text=message_text)

    return {
        'statusCode': 200
    }
