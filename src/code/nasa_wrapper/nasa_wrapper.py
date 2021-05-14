import requests
import json


def get_earth_events(params=None):

    url = "https://eonet.sci.gsfc.nasa.gov/api/v3/events"
    full_url = url + \
        f"?status={params.get('status')}&days={params.get('days')}"

    resp = requests.get(url)

    return resp.json()
