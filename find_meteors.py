import math
import requests

def calc_dist(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    h = math.sin( (lat2 - lat1) / 2 ) ** 2 + \
      math.cos(lat1) * \
      math.cos(lat2) * \
      math.sin( (lon2 - lon1) / 2 ) ** 2

    return 6372.8 * 2 * math.asin(math.sqrt(h))

meteor_resp = requests.get('https://data.nasa.gov/resource/gh4g-9sfh.json')
print(meteor_resp.status_code)

meteor_data = meteor_resp.json()

print(meteor_data[0])
print(calc_dist(50.775000,6.083330, 30.833330,-97.766670))
my_loc = (30.833330,-97.766670)
print(float(meteor_data[0]['reclat']))
#for meteor in meteor_data:
    #meteor['distance'] = calc_dist(float(meteor['reclat']), float(meteor['reclong']),my_loc[0], my_loc[1])

#print(meteor_data[0]['reclat'])
#for meteor in meteor_data:
#    print(meteor)
#    meteor['distance'] = calc_dist(float(meteor['reclat']), float(meteor['reclong']),my_loc[0], my_loc[1])

#meteor_data[0].get('reclat',0)

for meteor in meteor_data:
    if not('reclat' in meteor and 'reclong' in meteor):
        continue
    meteor['distance'] = calc_dist(float(meteor['reclat']), float(meteor['reclong']),my_loc[0], my_loc[1])
    print(meteor['distance'])
#if 'reclat' not in meteor or 'reclong' not in meteor:continue

print(meteor_data[0])

list = [1, 3, -5, 0]
list.sort()
print(list)

def get_dist(meteor):
    return meteor.get('distance', math.inf)

print(meteor_data[0])

#print(meteor_data.sort(key=get_dist))

print(meteor_data[0:10])
print(meteor_data[0])
print(meteor_data[-1:-11:-1])
print(len(meteor_data))

print(len([ m for m in meteor_data if 'distance' not in m ]))

count = 0
for m in meteor_data:
    if 'distance' not in m:
        count += 1
print(count)

##test

