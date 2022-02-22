# Author: Caden Kroonenberg
# Date: 2-21-22

import spotipy
import yaml
import pprint
import datetime as dt

with open("spotify_details.yml", 'r') as stream:  
    spotify_details = yaml.safe_load(stream)

pp = pprint.PrettyPrinter(indent=4)

# https://developer.spotify.com/web-api/using-scopes/
scope = "user-library-modify user-follow-read user-top-read playlist-modify-public user-read-currently-playing user-modify-playback-state"

sp = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(
    client_id=spotify_details['client_id'],
    client_secret=spotify_details['client_secret'],
    redirect_uri=spotify_details['redirect_uri'],    
    scope=scope)
)

# Artist URI
nav = sp.artist(spotify_details['nav']) # spotify_details['nav'] = NAV URI
# Top 10 tracks
nav_tracks = sp.artist_top_tracks(spotify_details['nav'])['tracks']

# Create navify playlist
playlist_title = 'navify_test' + str(dt.datetime.now())
playlist = sp.user_playlist_create('cskberg', playlist_title, public=True, collaborative=False, description='')
pid = playlist['id'] # Playlist ID

# Add top tracks to playlist and queue
for nt in nav_tracks:
    sp.playlist_add_items(playlist_id=pid, items=[nt['id']], position=None)
    sp.add_to_queue(uri=nt['id'], device_id=None)
    print('{}\t{}'.format(nt['name'], nt['id']))

# Start enqueued songs
sp.next_track(device_id=None)
