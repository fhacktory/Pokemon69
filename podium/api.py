from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import io
import json

def get_info(city, job):
    raw_fb = get_facebook(city, job)
    raw_yelp = get_yelp(city, job)
    raw = merge_api(raw_fb, raw_yelp)
    return raw

def get_facebook(city, job):
    return []

def get_yelp(city, job):
    print(city, job)
    with io.open('yelp.json') as cred:
        creds = json.load(cred)
        auth = Oauth1Authenticator(**creds)
        client = Client(auth)
    results = client.search(city, **{
        'term': job,
        'lang': 'fr'
    }).businesses
    res = []
    for result in results:
        res.append({
            "name": result.name,
            "rating": result.rating
        })
    return res

def merge_api(f, y):
    return y + f
