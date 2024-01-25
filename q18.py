# 18. Find a package in the Python standard library for dealing with
# JSON. Import the library module and inspect the attributes of the
# module. Use the help function to learn more about how to use the
# module. Serialize a dictionary mapping 'name' to your name and 'age'
# to your age, to a JSON string. Deserialize the JSON back into
# Python.

import json

# print(dir(json))
# print(help(json))
dummy_data = {"name": "Rohan", "Age":22}
json_convert = json.dumps(dummy_data, sort_keys=True, indent=4)
print(json_convert)
# 
# print(json.loads(json.dumps(["Dummy_Data", {"name": "Rohan", "Age":22}])))
decoded_json = json.loads(json_convert)
print(decoded_json)