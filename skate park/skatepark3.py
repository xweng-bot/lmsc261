import json


try:
    data_json = open("skaters.json")
    skaters = json.load(data_json)

except FileNotFoundError:
    print("File not found!")

def check_age_experience(skaters):

    for skater in skaters:
        name = skater.get("name")
        age = skater.get("age")
        is_experienced = skater.get("is_experienced")

        if age >= 13 and is_experienced:
            print(f"Hi {name}, welcome to the skate park!")

check_age_experience(skaters)