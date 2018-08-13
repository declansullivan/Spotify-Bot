import spotipy.util as util
import webbrowser, spotipy, json, time, sys, os

username = sys.argv[1]
scopes = 'user-read-currently-playing user-modify-playback-state'

# export SPOTIPY_CLIENT_ID='09268da821f04cf6b2375e2118ea29b4'
# export SPOTIPY_CLIENT_SECRET='5701869a816c454ebfc89247441edba9'
# export SPOTIPY_REDIRECT_URI='http://google.com/'

try:
    token = util.prompt_for_user_token(username, scopes)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scopes)

spotify = spotipy.Spotify(auth=token)

previous_song = None

while True:
    current_song = spotify.current_user_playing_track()['item']
    current_name = current_song['name']
    if previous_song != current_song:
        print(current_song['name'])
        previous_song = current_song
        current_album = spotify.album(current_song['album']['uri'])
        if 'christmas' in current_album['name'].lower():
            spotify.next_track()