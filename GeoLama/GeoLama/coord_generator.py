import google_streetview.api
import requests
import json
import googlemaps

def get_random_city_coordinates():
  resp = requests.get("https://api.3geonames.org/?randomland=yes&json=1")
  json = resp.json()

  gmaps = googlemaps.Client(key="AIzaSyAlpAWZzY0kUfxMZxRP-j6EpiJyyMuxBpE")
  try:
    # Geocoding an address
    geocode_result = gmaps.geocode(json['major']['city'])
    coor = '{0},{1}'.format(geocode_result[0]['geometry']['location']['lat'],
                            geocode_result[0]['geometry']['location']['lng'])
  except Exception as e:
    print("wtf_lol")
    return None
  return coor

# Define parameters for street view api
params = [{
  'size': '600x300', # max 640x640 pixels
  'location': '46.414382,10.013988',
  'heading': '0',
  'pitch': '0',
  'key': 'AIzaSyAlpAWZzY0kUfxMZxRP-j6EpiJyyMuxBpE'
}]

number_of_panos = 0
dict_of_coord = {}
dict_of_coord["panoCoordinates"] = []

while number_of_panos != 10:

  params[0]['location'] = get_random_city_coordinates()

  # Create a results object
  try:
    results = google_streetview.api.results(params)
    results.preview()
    lng_ltd = params[0]["location"].split(',')
    print(lng_ltd)
    coord = {}
    coord['longitude'] = lng_ltd[0]
    coord['latitude'] = lng_ltd[1]
    dict_of_coord["panoCoordinates"].append(coord)
    number_of_panos += 1
  except Exception as panoException:
    print("No pano")
    continue

print(dict_of_coord)
with open('pano_coords.json','w') as outfile:
    json.dump(dict_of_coord, outfile)

