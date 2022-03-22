import json
import sys

import tweepy
from message_puller import get_message


def main():
    message = get_message()

    with open("secrets.json") as f:
        secrets = json.load(f)

    client = tweepy.Client(
        consumer_key=secrets["consumer_key"],
        consumer_secret=secrets["consumer_secret"],
        access_token=secrets["access_token"],
        access_token_secret=secrets["access_token_secret"],
    )

    try:
        resp = client.create_tweet(text=message)
    except Exception as e:
        sys.stderr.write(f'{e}\n')
    else:
        print(resp)


if __name__ == '__main__':
    sys.exit(main())
