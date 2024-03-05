import os # we can access environment variables with this library
import pandas as pd
import matplotlib.pyplot as plt
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials # method that takes care of the credentials
from dotenv import load_dotenv
load_dotenv()

# client_id = os.environ.get("CLIENT_ID")
# client_secret = os.environ.get("CLIENT_SECRET") Credentials makes this

artists_id = "spotify:artist:4wck1fvaBpmJNFaeDT1Laa" # constant: variable you are not planning to change
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.artist_top_tracks(artists_id) # method is from spotipy, gets 10 results
print(results.keys()) # gives back the top level keys of the .json: in this keys is only tracks
# print(results["tracks"].keys()), gives back a list of tracks (keys cannot be an attribute of a list so if we try -> error)
first_element_tracks = results["tracks"][0]
# print(first_element_tracks.keys()) # keys of a singular track, in this case the one on index 0
print(first_element_tracks["popularity"])

tracks = results["tracks"] # to get the first ten elements of the list (python slice for lists and strings)
df = pd.DataFrame(tracks, columns = ["name", "popularity", "duration_ms"]) # DataFrame works with csv, json, lists etc
print(df)

df_popular = df.sort_values(by=["popularity"])[-3:] # sort DataFrame for popularity
print(df_popular)

duration_points = df.duration_ms
# print(duration_points)
popularity_points = df.popularity
plt.plot(duration_points, popularity_points)
plt.show()

import seaborn as sns

scatter_plot = sns.scatterplot(data = df, x = "popularity", y = "duration_ms")
fig = scatter_plot.get_figure()
fig.savefig("scatter_plot.png")