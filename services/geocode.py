import requests

def geocode(address):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json"
    }
    r = requests.get(url, params=params).json()
    if r:
        return float(r[0]["lat"]), float(r[0]["lon"])
    return None, None
def reverse_geocode(lat, lon):
    url = "https://nominatim.openstreetmap.org/reverse"
    params = {
        "lat": lat,
        "lon": lon,
        "format": "json"
    }
    r = requests.get(url, params=params).json()
    if "address" in r:
        return r["address"]
    return None