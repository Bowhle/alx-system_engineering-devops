#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=None, after="", count=0):
    """
    Recursively retrieves hot articles from a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): A list to store hot article titles.
        after (str, optional): The ID of the last post retrieved.
        count (int, optional): The number of posts retrieved so far.

    Returns:
        list: A list containing the titles of all hot articles,
              or None if the subreddit is invalid.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/your_username)"
    }
    params = {"after": after, "count": count, "limit": 100}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code == 404:
        return None

    results = response.json().get("data", {})
    after = results.get("after")
    count += results.get("dist", 0)

    for child in results.get("children", []):
        hot_list.append(child.get("data", {}).get("title", ""))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
