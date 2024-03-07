#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers to a certain subreddit.
    """
    url = "https://oauth.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'script:subscriber_counter_v0.1 by /u/tarekElaasri'
    }
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        return res.json()['data']['subscribers']
    else:
        return 0
