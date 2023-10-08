import json
import os
import asyncio
import io
import requests
from social_modules.twitter import TwitterModule
from social_modules.mastodon import MastodonModule

tg_api_key = os.environ.get('TG_API_KEY')
channel_id = int(os.environ.get('CHANNEL_ID'))

tweepy_access_token = os.environ.get('X_ACCESS_TOKEN')
mastodon_client_id = os.environ.get('MASTODON_CLIENT_ID')

def get_photo_file(photo):
    file_response = requests.get(f"https://api.telegram.org/bot{tg_api_key}/getFile?file_id={photo['file_id']}")
    file = file_response.json()
    image_response = requests.get(f"https://api.telegram.org/file/bot{tg_api_key}/{file['result']['file_path']}")
    return io.BytesIO(image_response.content), file['result']['file_path'].split('/')[-1]

async def post(modules, text, photo, filename):
    tasks = [module.post(text, photo, filename) for module in modules]
    return await asyncio.gather(*tasks)

def lambda_handler(event, context):
    tg_event = json.loads(event['body'])
    print(tg_event)
    modules = []

    if tweepy_access_token is not None:
        modules.append(TwitterModule())

    if mastodon_client_id is not None:
        modules.append(MastodonModule())
    
    if 'channel_post' in tg_event and tg_event['channel_post']['chat']['id'] == channel_id:
        # Text-only messages will use the 'text' key
        message_text = tg_event['channel_post']['text'] if 'text' in tg_event['channel_post'] else None

        # Images will use 'caption'.  Get the image as a file
        photo_file, photo_filename = get_photo_file(tg_event['channel_post']['photo'][-1]) if 'photo' in tg_event['channel_post'] else (None, None)
        if photo_file is not None:
            message_text = tg_event['channel_post']['caption'] if 'caption' in tg_event['channel_post'] else message_text

        loop = asyncio.get_event_loop()
        loop.run_until_complete(post(modules, message_text, photo_file, photo_filename))

        if photo_file is not None:
            photo_file.close()

    return {
        'statusCode': 200
    }
