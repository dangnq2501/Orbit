import json

def exporter(filename, jsoned):
    return json.dumps(jsoned, indent=4)
