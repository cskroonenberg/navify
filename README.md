# navify

## About this project
This project was made to investigate the Spotify API with the [Spotipy](https://spotipy.readthedocs.io/en/2.18.0/#) Python library.

This project WILL write to your Spotify profile. It's main function is creating a playlist with NAV's current top 10 songs. After the playlist is made, the songs will be enqueued and played.

## Getting started
First we need to clone this repo:
1. Open your terminal
2. Run the commands `git clone https://github.com/cskroonenberg/navify && cd navify` to clone the repo and enter the root directory

In order to get started with our masterful playlist creation we need to access the Spotify API:
1. Create a [Spotify for Developers](https://developer.spotify.com/) account
2. From the [dashboard](https://developer.spotify.com/dashboard/login) setup a project (needed for API access)
3. Retrieve the client ID, client secret, and setup the redirect URI (as a local projects I set this to http://localhost:9001/callback)
4. Review the API documentation
5. Copy the `spotify_details.yml` file in the `sample` directory to the root directory of this project
6. Store your Client ID and Client Secret in the appropriate areas

Next, we'll need to install the required Python modules (I used Python 3.8.8):
1. Run `pip install -r requirements.txt` from the root directory

Finally, you're ready to experience magic:
1. `python navify.py`
