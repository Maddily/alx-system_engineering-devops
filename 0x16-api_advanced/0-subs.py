#!/usr/bin/python3
"""Query the Reddit API"""

import requests


def number_of_subscribers(subreddit):
    """Query the Reddit API and return the number
    of subscribers for a given subreddit."""

    headers = {'User-Agent': 'Mozilla/5.0'}

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
