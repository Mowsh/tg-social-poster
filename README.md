# tg-social-poster
AWS Lambda to post Telegram channel posts to various social networks.

## Configuration
This bot is configured through environment variables on the Lambda.

### Basic
- `TG_API_KEY` - Telegram bot's full API key (required)
- `CHANNEL_ID` - Channel ID for this bot to copy messages from (required)

### X/Twitter (Optional)
Set the following environment variables:

- `X_CONSUMER_KEY` - App API key
- `X_CONSUMER_SECRET` - App API secret
- `X_BEARER_TOKEN` - User bearer token
- `X_ACCESS_TOKEN` - User access token.  Ensure user has read/write privileges
- `X_ACCESS_TOKEN_SECRET` - User access token secret.  Ensure user has read/write privileges

### Mastodon (Optional)
Set the following environment variables:

- `MASTODON_CLIENT_ID` - App client ID
- `MASTODON_CLIENT_SECRET` - App client secret
- `MASTODON_ACCESS_TOKEN` - Your access token
- `MASTODON_BASE_URL` - Your Mastodon instance's URL

### Bluesky (Optional)
Set the following environment variables:

- `BLUESKY_HANDLE` - Bluesky handle
- `BLUESKY_PASSWORD` - Bluesky password, it's recommended to use an app password here

## Building

First, pull dependencies for your Lambda's arch, as described [here](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html#python-package-native-libraries).

Then run ./zip.sh in the project root to create a function.zip which can be uploaded to AWS Lambda.
