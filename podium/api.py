from    facebook                    import GraphAPI
from    json                        import load
from    io                          import open
from    yelp.client                 import Client
from    yelp.oauth1_authenticator   import Oauth1Authenticator
from    difflib                     import SequenceMatcher

def get_info(city, job):
    if (job and city):
        raw_fb = get_facebook(city, job)
        raw_yelp = get_yelp(city, job)
        return merge_api(raw_fb, raw_yelp, job)
    else:
        return []

def get_facebook(city, job):
    r = []

    # get your token here: https://developers.facebook.com/tools/explorer/
    access_token = 'CAACEdEose0cBAKQDlNnOCm5i8sMrWyamZBshacElzxaoUfdQdLKZCkBPCVnsmqhF73jVVJAZA6x5vJpgjRSWMCZB2U1DRaSFD32b0uZCZAXunFSM4KUPtCK8UfD0xWTDHM528VTW6ekYqOsos4PiujaU6PHEHZClZCbL4ZBsMZCmLwZC3IiPJXSwFoZAlVhJ0Mg3ifRJYBpGS8ZA6qAZDZD'
    g = GraphAPI(access_token)

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
    return res['data']


def fb_get_info(g, s):
    res = []
    for t in s:
        c = g.get_object(t['id'])
        res.append({
            'name': c.get('name'),
            'likes': c.get('likes'),
            'lon': c.get('location').get('longitude') if c.get('location') else 0,
            'lat': c.get('location').get('latitude') if c.get('location') else 0,
            'street': c.get('street'),
            'phone': c.get('phone'),
            'link': c.get('link'),
            'talking_about_count': c.get('talking_about_count'),
            'checkins': c.get('checkins')
        })
    return res

def get_yelp(city, job):
    res = []

    with open('yelp.json') as cred:
        creds = load(cred)
        auth = Oauth1Authenticator(**creds)
        client = Client(auth)

    results = client.search(city, **{
        'term': job,
        'lang': 'fr',
        'sort': 2
    }).businesses

    for result in results:
        res.append({
            "name": result.name,
            "rating": result.rating,
            "longitude": result.location.coordinate.longitude,
            "latitude": result.location.coordinate.latitude,
            "street": result.location.address
        })

    return res

def merge_api(f_results, y_results, job):
    res = [];
    def merge(y_res, f_res):
        res.append({
            'name': y_res.get('name'),
            'facebook': {
                'name': f_res.get('name'),
                'likes': f_res.get('likes')
            },
            'yelp': {
                'name': y_res.get('name'),
                'rating': y_res.get('rating')
            }
        })

    for y_res in y_results:
        for f_res in f_results:
            if (f_res.get('street') and y_res.get('street') and SequenceMatcher(None, f_res.get('street'), y_res.get('street')).ratio() > 0.80):
                merge(y_res, f_res)
                break
            elif (SequenceMatcher(None, f_res.get('name').replace(job, ''), y_res.get('name').replace(job, '')).ratio() > 0.80):
                merge(y_res, f_res)
                break
    return res