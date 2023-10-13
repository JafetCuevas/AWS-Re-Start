import json

def readJsonFile(file):
    data = ""
    try:
        with open(file) as jsonFile:
            data = json.load(jsonFile)
    except IOError:
        print("Couldn't read file")
    return data    

