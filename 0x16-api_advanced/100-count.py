#!/usr/bin/python3
"""Use a recursive function to query the Reddit API"""

import requests


def count_words(subreddit, word_list, after=None, occurrences=None):
    """Query the Reddit API recursively, parse the title of all hot articles,
    and print a sorted count of given keywords"""

    if occurrences is None:
        occurrences = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    parameters = {'limit': 100, 'after': after}
    response = requests.get(url,
                            headers=headers,
                            params=parameters,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    children = data.get('data', {}).get('children', [])

    for child in children:
        title = child.get('data', {}).get('title').lower().split()
        for word in word_list:
            word = word.lower()
            if word in title:
                if word in occurrences:
                    occurrences[word] += 1
                else:
                    occurrences[word] = title.count(word)

    after = data.get('data', {}).get('after')
    if after is not None:
        count_words(subreddit, word_list, after, occurrences)
    else:
        sorted_occurrences = sorted(occurrences.items(),
                                    key=lambda x: (-x[1], x[0]))

        for key, value in sorted_occurrences:
            print(f"{key}: {value}")
