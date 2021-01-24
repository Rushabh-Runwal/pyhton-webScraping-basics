import requests
from bs4 import BeautifulSoup
import argparse
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = ''
SPOTIFY_CLIENT_SECRETE  = ''
SPOTIFY_MY_APP_URL = ''

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRETE,
        show_dialog=True,
        cache_path="token.txt"))

user_id = sp.current_user()["id"]

date = input("Which day's playlist you wanna make ? (enter in (yyyy-mm-dd) format)  ")
billborad_url = f'https://www.billboard.com/charts/hot-100/{date}'

web_page = requests.get(billborad_url).text

soup = BeautifulSoup(web_page, "html.parser")
names = soup.find_all(name='span', class_="chart-element__information__song text--truncate color--primary")
names = [i.getText() for i in names]
songs_url = []
year = date.split('-')[0]
for song in names:
        result = sp.search(q=f'track: {song} year: {year}', type='track')
        # print(result)
        try:
                url= result["tracks"]["items"][0]["uri"]
                songs_url.append(url)
        except IndexError:
                print("Song not found")

playlist_name=f"{date} Billboard 100"
playlist = sp.user_playlist_create(user_id,playlist_name,False,False,f"Billboard top 100 of {date}")
print(playlist)
sp.playlist_add_items(playlist['id'],songs_url)