cache = {}

def get_cache(sector):
    return cache.get(sector)

def set_cache(sector, data):
    cache[sector] = data