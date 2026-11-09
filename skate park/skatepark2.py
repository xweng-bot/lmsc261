import json

data_json = open("ramps.json")
ramps = json.load(data_json)

print(ramps)

for key, value in ramps.items():
    print(key, value)

print(f"{key}s favorite ramp is {value}")