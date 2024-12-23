from spotipy.oauth2 import SpotifyClientCredentials,SpotifyOAuth
import spotipy
import pandas as pd
import random
import math
client_id = "12308f6c7b9c4194a6ca9e06f43d3bfd"
client_secret = "e27a673a043147df8bf4a5d0a9fe8084"
#scope = "user-library-read"
username = "31nfsp7vapk4zh24xzvw3lkavx5e"
redirect_uri = 'https://juliascodingeckle.pythonanywhere.com/spoti/callback'
scope = 'user-read-recently-played user-library-read user-top-read'

import requests
from datetime import datetime
from typing import List
import spotipy.util as util
from os import listdir
import warnings
warnings.filterwarnings("ignore")
client_credentials_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
