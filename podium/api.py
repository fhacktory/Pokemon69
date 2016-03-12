import facebook
import requests
import json
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
    r = []

    # get your token here: https://developers.facebook.com/tools/explorer/
    access_token = 'CAACEdEose0cBAONm8sTTAyk3iBSLkTAFkkSlmzP2PZCx1WIldnG9iqcL0mkAgoJHDMeUiZBFD5hmFe0yPmZA2f9BHhRHFu2i8yNoZCN77SdggazS0I4bHYnAkG4RFw6zo0qc9cJcKtYjUXB7vRT2szSxmTLmZB5ff70hp3BRmdqiYcfUCmF6RRWTCRO5x8qqzH0bCLwFZBvwZDZD'
    g = facebook.GraphAPI(access_token)

    s = fb_search_pages(g, city, job)
    r = fb_get_info(g,s)

    return r


def fb_search_pages(g, city, job):
    # TODO : seulement la bonne categorie
    # TODO : plusieurs pages
    res = []

    q = job + ' in ' + city
    res = g.request('search', {'q': q, 'type': 'page'})
    # [fb_some_action(post=post) for post in posts['data']]
    # posts = requests.get(posts['paging']['next']).json()
    #print json.dumps(res)
    return res['data']


def fb_get_info(g, s):
    res = []
    for t in s:
        c = g.get_object(t['id'])
        res.append({
            'name': c['name'],
            'likes': c['likes'],
            'lon': c['location']['longitude'],
            'lat': c['location']['latitude'],
            'phone': c['phone'],
            'link': c['link'],
            'name': c['name'],
            'talking_about_count': c['talking_about_count'],
            'checkins': c['checkins']
            })
    return res

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