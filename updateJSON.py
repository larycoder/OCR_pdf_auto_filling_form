import json
import argparse

def ParJson2Dict(path_to_file_json):
  with open(path_to_file_json) as json_file:
    data = json.load(json_file)
    return data

ap = argparse.ArgumentParser()
ap.add_argument('-t', '--template', required=True, help='Input JSON file')
ap.add_argument('-i', '-input', required=True, help='Input text file')
ap.add_argument('-o', '--output', required=True, help='Output JSON file')

Dict = ParJson2Dict()
file = open(args['input'], 'r')
lines = []
for line in file:
  lines.append(line)
file.close()
for i in range(:len(lines)):
  Dict['WaL0'][i]['fill_val'] = lines[i]

with open(args['output'], 'w') as outfile:
  json.dump(Dict, outfile)

