import tweepy
import logging
import data

logger = logging.getLogger()


def create_api():
    auth = tweepy.OAuthHandler(
        data.CONSUMER_KEY, data.CONSUMER_SECRET)
    auth.set_access_token(data.OAUTH_TOKEN,
                          data.OAUTH_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
