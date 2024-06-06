#!/usr/bin/python3
'''
    This module contains the function top_ten
'''
import requests
from sys import argv

def top_ten(subreddit):
    '''
        Returns the top ten posts for a given subreddit
    '''
    user = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    
    try:
        response = requests.get(url, headers=user, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        data = response.json()
        posts = data.get('data', {}).get('children', [])
        if not posts:
            print(None)
            return

        for post in posts:
            print(post.get('data', {}).get('title'))

    except Exception:
        print(None)

if __name__ == "__main__":
    if len(argv) > 1:
        top_ten(argv[1])
    else:
        print(None)

