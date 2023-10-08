from atproto import Client, models
import os
from social_modules.social_interface import SocialModuleInterface

bluesky_handle = os.environ.get('BLUESKY_HANDLE')
bluesky_password = os.environ.get('BLUESKY_PASSWORD')

class BlueskyModule(SocialModuleInterface):
    async def post(self, text, photo, filename):
        try:
            client = Client()
            client.login(bluesky_handle, bluesky_password)

            post_text = text if text is not None else ""

            if photo is not None:
                client.send_image(post_text, photo, "")

                photo.close()
            else:
                client.send_post(post_text)

        except Exception as error:
            print("Bluesky error", error)
        