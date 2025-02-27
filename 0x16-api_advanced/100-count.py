#!/usr/bin/python3
"""
Function to count words in all hot posts of a given Reddit subreddit.
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API, parses the title of all
    hot articles, and prints a sorted count of given keywords.

    Args:
        subreddit (str): The subreddit to query.
        word_list (list): List of words to count occurrences of.
        after (str, optional): ID of the last post retrieved.
        counts (dict, optional): Dictionary storing word counts.

    Returns:
        None: Prints word counts in descending order.
    """
    if counts is None:
        counts = {}

    if not word_list or not subreddit:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100}

    if after:
        params["after"] = after

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    children = data.get("children", [])

    for post in children:
        title = post.get("data", {}).get("title", "").lower()
        for word in word_list:
            word_lower = word.lower()
            count = title.count(word_lower)
            if count:
                counts[word_lower] = counts.get(word_lower, 0) + count

    after = data.get("after")
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
