#!/usr/bin/python3

"""top_ten"""


def top_ten(subreddit):
    """get top ten hot titles of a certain subreddit """

    import requests

    url = "https://oauth.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent':
               'script:subscriber_counter_v0.1 by /u/tarekElaasri'
               }
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        if res.status_code == 200:
            titles = [item['data']['title']
                      for item in res.json()['data']['children']
                      if item['kind'] == 't3']
            for title in titles:
                print(title)
        else:
            return 0
