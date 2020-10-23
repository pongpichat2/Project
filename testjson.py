import json

a_file = open("Time.json", "r")
json_object = json.load(a_file)

data = json_object["TimeManhattan"]

for time in data:
    time["TimeText"] = 500
    time["timedistance"] = 200

a_file = open("Time.json", "w")
json.dump(json_object, a_file)
a_file.close()