#!/usr/bin/python3
"""Use a recursive function to query the Reddit API"""

import requests


""" def recursively_query(data, hot_list, i):
    Helper for recurse function

    hot_list[i] = data['data']['children'][i]['data']['title']
    recursively_query(data, hot_list, i + 1) """


def recurse(subreddit, hot_list=[], after=None):
    """Recursively query the Reddit API and return
     a list containing the titles of all hot articles
     for a given subreddit."""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    parameters = {'limit': 100, 'after': after}
    response = requests.get(url,
                            headers=headers,
                            params=parameters,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    children = data.get('data', {}).get('children', [])

    for child in children:
        title = child.get('data', {}).get('title')
        hot_list.append(title)

    after = data.get('data', {}).get('after')
    if after is not None:
        recurse(subreddit, hot_list, after)

    return hot_list
