import json

def get_test_data():
    with open("TestData/testdata.json", "r") as testdatafile:
        return json.load(testdatafile)