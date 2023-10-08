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
