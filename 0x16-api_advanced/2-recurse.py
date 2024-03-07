#!/usr/bin/python3

"""top_ten"""


def recurse(subreddit, hot_list=[], count=0, af=None):
    """get top ten hot titles of a certain subreddit """

    import requests

    url = "https://oauth.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent':
               'script:subscriber_counter_v0.1 by /u/tarekElaasri'
               }
    res = requests.get(url, headers=headers, allow_redirects=False,
                       params={"count": count, "after": af})

    if res.status_code == 200:
        if res.status_code == 200:
            hot = hot_list + ([item['data']['title']
                      for item in res.json()['data']['children']])
        info = res.json()
        if not info.get("data").get("after"):
            return hot
        return recurse(subreddit, hot_list, info.get('data').get('count'), info['data']['after'])
    else:
        return 0
