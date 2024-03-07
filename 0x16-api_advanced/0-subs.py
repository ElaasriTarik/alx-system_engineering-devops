#!/usr/bin/python3
import requests
from requests import *
"""number_of_subscribers"""


def number_of_subscribers(subreddit):
    """get number of subscribers to a certain subreddit """
    client_id = "PpEfMsSxFbxQHsIMzr5faQ"
    client_secret = "8yTk0bJrYf78NPzdONjt1zWRmYo8SQ"
    r_usr = "tarekElaasri"
    r_pass = "(k4r9CQ^^?wN46L"
    url = "https://www.reddit.com/api/v1/access_token"
    auth_data = {"grant_type": "password", "username": r_usr,
                 "password": r_pass}
    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    header = {'user-agent':
              'script:subscriber_counter_v0.1 by /u/tarekElaasri'}
    res = requests.post(url, data=auth_data,
                        headers=header,
                        auth=auth)

    if res.status_code == 200:
        token = res.json()['access_token']
    else:
        print(res)

    url = "https://oauth.reddit.com/r/{}/about".format(subreddit)
    headers = {'Authorization': 'bearer ' + token,
               'User-Agent':
               'script:subscriber_counter_v0.1 by /u/tarekElaasri'}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        return res.json()['data']['subscribers']
    else:
        return 0
