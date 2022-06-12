import sys
import json
import requests

search_terms = [arg for arg in sys.argv[1:]]
query = f"https://vid.puffyan.us/api/v1/search?q={search_terms}&pretty=1"

response = requests.get(query)
response_json = response.json()
video_id = response_json[0]["videoId"]
video_url = f"https://www.youtube.com/watch?v={video_id}"
# The print gets fed into the bash script
print(video_url)