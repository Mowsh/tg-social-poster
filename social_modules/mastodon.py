from mastodon import Mastodon
import os
import mimetypes
from social_modules.social_interface import SocialModuleInterface

mastodon_client_id = os.environ.get('MASTODON_CLIENT_ID')
mastodon_client_secret = os.environ.get('MASTODON_CLIENT_SECRET')
mastodon_access_token = os.environ.get('MASTODON_ACCESS_TOKEN')
mastodon_base_url = os.environ.get('MASTODON_BASE_URL')

class MastodonModule(SocialModuleInterface):
    async def post(self, text, photo, filename):
        try:
            mastodon = Mastodon(
                client_id=mastodon_client_id,
                client_secret=mastodon_client_secret,
                access_token=mastodon_access_token,
                api_base_url=mastodon_base_url
            )

            media_ids = None
            if photo is not None:
                mime_type, _ = mimetypes.guess_type(filename)
                media = mastodon.media_post(photo, file_name=filename, mime_type=mime_type)
                media_ids = [media['id']]

            mastodon.status_post(text, media_ids=media_ids)
        except Exception as error:
            print("Mastodon error", error)
        