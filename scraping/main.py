import os
import csv
from dotenv import load_dotenv
import spotipy
import lyricsgenius as lg
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd


load_dotenv()

spotify_client_id = os.getenv("CLIENT_ID")
spotify_client_secret = os.getenv("CLIENT_SECRET")
spotify_redirect_uri=os.getenv("REDIRECT_URI")
genius_access_token=os.getenv("GENIUS_ACCESS_TOKEN")

genius=lg.Genius(genius_access_token)
track_names=[]
songs_lyrics=[]
artists_names=[]

playlist_links={
    "80'ler Türkçe":"https://open.spotify.com/playlist/37i9dQZF1DX4io1yPyoLtv?si=7fd2d5fefa944bf7",
    "90'lar Türkçe":"https://open.spotify.com/playlist/37i9dQZF1DXb7MJRXLczzR?si=426a69805849461d",
    "2000'ler Türkçe":"https://open.spotify.com/playlist/37i9dQZF1DWYteTcNVQZNq?si=47be4cafcd824efc",
    "2010'lar Türkçe":"hhttps://open.spotify.com/playlist/37i9dQZF1DXaE9T4Nls8eC?si=5876fd4ec08542c1",
    "Altüst":"https://open.spotify.com/playlist/37i9dQZF1DWXHrHoo7qtCf?si=438d53eb9fa14d17",
    "2023 Türkçe":"https://open.spotify.com/playlist/37i9dQZF1DX2BRJ8oOzeOL?si=8ee6220774e3495a"
    }


client_credentials_manager = SpotifyClientCredentials(client_id=spotify_client_id, client_secret=spotify_client_secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def get_playlist_URI(playlist_link):
    playlist_URI = playlist_link.split("/")[-1].split("?")[0]
    return playlist_URI

for key,value in playlist_links.items():
    playlist_URI=get_playlist_URI(value)

    for track in sp.playlist_tracks(playlist_URI)["items"]:
    
        #Track name
        track_name = track["track"]["name"]
        
        #Artist's Name
        artist_name = track["track"]["artists"][0]["name"]
    
        song=genius.search_song(title=track_name,artist=artist_name)
        if song is not None and isinstance(song.lyrics, str) and song.lyrics.strip():
            artists_names.append(artist_name)
            track_names.append(track_name)
            lyrics = song.lyrics  # 'lyrics' özelliği olmayan bir nesneye erişmeye çalışılıyorsa hata alınır.
            songs_lyrics.append(lyrics)
        
    
    df=pd.DataFrame({"Artist's Name":artists_names,"Song Name":track_names,"Lyric":songs_lyrics})
    df.to_excel(key+".xlsx",index=False)