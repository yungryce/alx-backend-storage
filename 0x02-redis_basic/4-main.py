#!/usr/bin/env python3
from time import time
from urllib.parse import urlencode
from urllib.request import urlopen

# Import the decorated function
get_page = __import__('web').get_page

# URLs to test
urls = [
    "http://slowwly.robertomurray.co.uk/delay/1000/url/http://www.example.com",
    "http://slowwly.robertomurray.co.uk/delay/1000/url/http://www.example.org",
]

def test_cache(url):
    print(f"Requesting URL: {url}")

    # Measure time taken to fetch the page
    start_time = time()
    html = get_page(url)
    end_time = time()

    print(f"Time taken: {end_time - start_time:.2f} seconds")
    print(f"HTML content length: {len(html)}")
    print("-" * 30)

# Test each URL
for url in urls:
    test_cache(url)

