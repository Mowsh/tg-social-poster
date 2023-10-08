# tg-social-poster
AWS Lambda function to post Telegram channel posts to various social networks.

## Installation
1. Download the latest release zip file for your arch from [here](https://github.com/Mowsh/tg-social-poster/releases).
2. Create a bot on Telegram using the [BotFather](https://t.me/BotFather) to get an API key.
3. Put the bot in the channel you want to post from.
3. Create an Lambda in AWS, and upload the zip archive as the source.
4. Create an API Gateway in AWS, and have it trigger the Lambda.
5. Use Telegram's [`setWebhook`](https://core.telegram.org/bots/api#setwebhook) API to point the bot at your API Gateway URL.
6. Fill in the required configuration below, and any configuration for social media platforms you want to use.

## Configuration
This bot is configured through environment variables on the Lambda.

### Basic
- `TG_API_KEY` - Telegram bot's full API key (required)
- `CHANNEL_ID` - Channel ID for this bot to copy messages from (required)
- `IGNORE_STRING` - If your post contains this string, the bot will ignore it and not post it to any social networks.

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

## Limitations
- This is not able to post more than one photo at a time, because albums come through as multiple callbacks and Lambdas are stateless by design, so no way of tracking when an album has finished being sent.
- Videos are currently not supported, Bluesky doesn't allow posting them anyway.
