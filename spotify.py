import requests
import json
import re
import os

# Fetch environment variables
CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

# Spotify API URLs
AUTH_URL = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1/'

# Request authorization token
auth_response = requests.post(AUTH_URL, {
   'grant_type': 'client_credentials',
   'client_id': CLIENT_ID,
   'client_secret': CLIENT_SECRET,
})

# Check if authorization successful
if auth_response.status_code == 200:
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}
else:
    print(f"Failed to retrieve access token: {auth_response.status_code}")
    print(auth_response.text)
    exit()

# Initialize seed tracks variable
seed_tracks = ''

# Take in 5 seed track URLs through user input
for i in range(5):
    curr_url = input(f'Enter track {i+1} URL: ')

    # Use regex to find the track_id in the URL provided by the user
    match = re.search(r'track/(\w+)', curr_url)
    if match:
        curr_track_id = match.group(1)
    else:
        print(f'Invalid URL format: {curr_url}')
        continue

    # Append track_id to seed_tracks list
    if seed_tracks:
        seed_tracks += ',' + curr_track_id
    else:
        seed_tracks = curr_track_id

print('seed_tracks: ' + seed_tracks + '\n')

# Make GET request to Spotify API for recommendations based on seed tracks
recommendations_url = BASE_URL + 'recommendations?seed_tracks=' + seed_tracks
response = requests.get(recommendations_url, headers=headers)

# Check response status and handle data
if response.status_code == 200:
    json_data = response.json()

    # Print artist names and links to their Spotify pages
    for track in json_data['tracks']:
        for artist in track['album']['artists']:
            print(f"{artist['name']}: {artist['external_urls']['spotify']}")
else:
    print(f"Failed to retrieve recommendations: {response.status_code}")
    print(response.text)