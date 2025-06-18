def prepareGraph(filepath, json_dump):
    with open(filepath, 'w') as f:
        f.write("var rendru = " + json_dump)