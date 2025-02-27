#!/usr/bin/python3
"""A function that queries the Reddit API and prints
   the titles of the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """Print the top 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'api/advanced, task1'}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        results = data.get("data")
        # Loop through and print the titles of the posts
        for post in results.get("children", []):
            print(post.get("data", {}).get("title"))
    else:
        print(None)
