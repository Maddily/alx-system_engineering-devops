#!/usr/bin/python3
"""Query the Reddit API"""

import requests


def top_ten(subreddit):
    """Query the Reddit API and print the titles
    of the first 10 hot posts listed for a given subreddit"""

    headers = {'User-Agent': 'Mozilla/5.0'}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        for i in range(10):
            print(data['data']['children'][i]['data']['title'])
    else:
        print(None)
