#!/usr/bin/python3
import requests
"""A function that queries the Reddit API and returns
   a list containing the titles of all hot articles for
   a given subreddit."""

def recurse(subreddit, hot_list=None):
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'api/advanced, task1'}
    params = {"limit": 100}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        children = data.get("data", {}).get("children", [])
        hot_list.extend([post["data"]["title"] for post in children])

        after = data.get("data", {}).get("after")
        if after:
            params['after'] = after
            return recurse(subreddit, hot_list)

        return hot_list
    return None
