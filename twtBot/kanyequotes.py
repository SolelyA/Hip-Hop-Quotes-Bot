import tweepy
import logging
from config import create_client
import time
from datetime import date
import requests
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def kanye_quotes(client):
    logger.info("Retriving a Kanye quote")
    response = requests.get('https://api.kanye.rest')
    quote = response.json()

    
    client.create_tweet(text=quote["quote"])


def main():
    client = create_client()
    while True:
        kanye_quotes(client)
        logger.info("Uploading the quote")
        time.sleep(60)


if __name__ == "__main__":
    main()