
def get_info(city, job):

    raw_fb = get_facebook(city, job)
    raw_yelp = get_yelp(city, job)
    raw = merge_api(raw_fb, raw_yelp)
    return raw

def get_facebook(city, job, raw):
    return raw

def get_yelp(city, job, raw):
    return raw

def merge_api(f, y):
    return y + f
