#!/usr/bin/python3
import requests
import re
"""A function that queries the Reddit API, 
    parses the title of all hot articles, and prints 
    a sorted count of given keywords."""

def count_words(subreddit, word_list, count_dict=None, after=None):
    if count_dict is None:
        count_dict = {word.lower(): 0 for word in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'api/advanced, task1'}
    params = {"limit": 100}
    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        children = data.get("data", {}).get("children", [])

        for post in children:
            title = post["data"]["title"].lower()
            for word in word_list:
                word_count = len(re.findall(r'\b' + re.escape(word.lower()) + r'\b', title))
                count_dict[word.lower()] += word_count

        after = data.get("data", {}).get("after")
        if after:
            return count_words(subreddit, word_list, count_dict, after)

        sorted_count = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))

        for word, count in sorted_count:
            if count > 0:
                print(f"{word}: {count}")
    else:
        return None
