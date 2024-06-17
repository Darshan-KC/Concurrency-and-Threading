# Write a python program to download multiple file concurrently using thread

import threading
import requests
import os

# function for downloading file
def download_file(url, dest_folder):
    local_file_name = os.path.join(dest_folder,url.split('/')[-1])
    
    # Make the HTTP request and stream the response content
    with requests.get(url,stream=True) as r:
        # Raise an HTTPError if the response was unsuccessful
        r.raise_for_status()
        
        # Open the local_file for writing
        
        with open(local_file_name,'wb') as f:
            # Iterate over the response data in chunks
            for chunk in r.iter_content(chunk_size=8192):
                # Write each chunk to the local file
                f.write(chunk)
            
        print(f"Downloaded {local_file_name}")
        
# Function to handle downloading multiple file concurrently
def concurrent_download(urls, dest_folder):
    pass
    
