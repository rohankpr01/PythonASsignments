import json

#Please place the input file in current working directory from where you will execute this code.

def remove_json_element(**name):
    obj = json.load(open("test_payload.json"))
    dictionary_array = [obj]
    for sub_dictionary in dictionary_array:
        if type(sub_dictionary) is dict:
            for key, value in sub_dictionary.items():
                 print("key=", key)
                 print("value", value)
                 if key == name['x'] or key == name['y']:
                     del sub_dictionary[key]
                     break

                 if type(value) is dict:
                     dictionary_array.append(value)

    open("updated-file.json", "w").write(
        json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
    )

#If you pass x="" and pass y="Any Key you want to delete it will delete that value"
#If you want tp pass x="Any Key" and y="" it will delete that key only

#here as per the assignment purpose i have passed both the key both will delete the keys in updated Json file

remove_json_element(x='outParams',y='appdate')


