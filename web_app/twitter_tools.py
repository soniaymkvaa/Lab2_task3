import tweepy
import json
from geopy.geocoders import Nominatim

CONSUMER_KEY = ''
CONSUMER_SEC = ''
ACCESS_TOK = ''
ACCESS_SEC = ''


def get_friends(screen_name):
    """
    returns list frends with screen names and coordinates(x,y)
    """
    friends = []
    if not (CONSUMER_KEY and CONSUMER_SEC and ACCESS_TOK and ACCESS_SEC):
        print('One or more twitter api values are missing. Using template json file.')
        api_data = []
        with open('friends.json', 'r', encoding='utf8') as template:
            api_data = json.load(template)['users']
    else:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SEC)
        auth.set_access_token(ACCESS_TOK, ACCESS_SEC)
        api = tweepy.API(auth)
        api_data = api.friends(screen_name)
    geolocator = Nominatim(user_agent='myserver@myserver.com')
    for friend in api_data:
        loc = geolocator.geocode(friend['location'])
        if not loc:
            continue
        friends.append({
            'screen_name': friend['screen_name'],
            'longitude': loc.longitude,
            'latitude':  loc.latitude,
        })
    return friends
