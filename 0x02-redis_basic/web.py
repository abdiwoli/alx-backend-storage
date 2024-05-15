#!/usr/bin/env python3
""" module documentation """
from datetime import datetime, timedelta
import requests

# Define a cache dictionary
cache = {}
cache_expiration = timedelta(seconds=10)


def update_cache(url, content):
    """ update the cache """
    cache["count:" + url] = cache.get("count:" + url, 0) + 1
    cache[url] = (content, datetime.utcnow())


def get_page(url):
    """Fetches the HTML contE ent of a URL with caching. """
    return requests.get(url).text


def cache_data(func):
    """ Decorator for caching functionality """
    def wrapper(url):
        content = get_page(url)
        return content

    return wrapper


@cache_data
def get_page_decorated(url):
    """Example usage with decorator """
    return get_page(url)
