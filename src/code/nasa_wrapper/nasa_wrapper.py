import requests
import json


def get_earth_events(params=None):
    """Wrapper over NASA Events that will return information related to
    the given filters. 

    args:
        - params: 
            status: , 
            days: the amount of days to search back (if None, will query all days), 
            category: the type of event --
                drought, wildfires, waterColor, volcanoes,
                temperatureExtremes, snow, severeStorms, seaAndLakeIce,
                manmade, landslides, floods, earthquakes, dustAndHaze"

    returns:
        - dictionary of events with related information for each event.

    """
    if params.get('status'):
        status = params.get('status').lower()
    if params.get('category'):
        category = params.get('category').lower()
    days = params.get('days')

    url = "https://eonet.sci.gsfc.nasa.gov/api/v3/events"
    full_url = url + \
        f"?status={status}&days={days}&category={category}"

    resp = requests.get(full_url)

    return resp.json()
