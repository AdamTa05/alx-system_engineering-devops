#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise HTTPError for bad responses
        
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data'].get('subscribers', 0)
            return subscribers
    except requests.exceptions.RequestException as e:
        # For debugging: print(e)
        pass

    return 0

