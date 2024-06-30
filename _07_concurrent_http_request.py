# Write a Python program that performs concurrent HTTP requests using threads.

import requests
import threading

def http_request(url):
    response = requests.get(url)
    print(f"Response from {url} : {response.status_code}")

def main() ->None:
    # List of URLs to make requests to
    urls = [
        "https://www.example.com",
        "https://www.google.com",
        "https://www.wikipedia.org",
        "https://www.python.org"
    ]
    
    # create a threads 
    threads = []
    
    for url in urls:
        thread = threading.Thread(target=http_request,args=(url,))
        thread.start()
        threads.append(thread)
        
    # Wait for all the threads
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()