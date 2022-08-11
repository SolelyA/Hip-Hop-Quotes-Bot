import tweepy
import logging
from dotenv import load_dotenv
import os

load_dotenv()
logger = logging.getLogger()

def create_client():
    client = tweepy.Client(consumer_key=os.getenv('consumer_key'),
                       consumer_secret=os.getenv('consumer_secret'),
                       access_token=os.getenv('access_token'),
                       access_token_secret=os.getenv('access_token_secret'))
    logger.info("client created")
            
    return client