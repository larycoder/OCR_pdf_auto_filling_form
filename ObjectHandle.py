from ImageProcess import extract_String_2_Dimension as s2d
import json

# create json object of field
def DictionaryCreate(path_to_field_name, path_to_field_position, path_to_file_json):
  # get values from file
  field_name = open(path_to_field_name,'r')
  position = open(path_to_field_position,'r')

  # dictionary of object
  Dictionary = {}
  Dictionary['WaL0'] = []

  # create field object
  for field_name_line in field_name:
    field_pos = position.readline()
    fill_pos = position.readline()
    (field_x1, field_y1, field_x2, field_y2) = s2d(field_pos)
    (fill_x1, fill_y1, fill_x2, fill_y2) = s2d(fill_pos)
    Object = {'field_name':field_name_line, 
              'field_pos':{'x1':field_x1, 'y1':field_y1, 'x2':field_x2, 'y2':field_y2},
              'fill_pos':{'x1':fill_x1, 'y1':fill_y1, 'x2':fill_x2, 'y2': fill_y2},
              'fill_val':'None' 
              }
    Dictionary['WaL0'].append(Object)
  # return dictionary
  with open(path_to_file_json, 'w') as outfile:
    json.dump(Dictionary, outfile)


import json
# parse json to dictionary
def ParJson2Dict(path_to_file_json):
  with open(path_to_file_json) as json_file:
    data = json.load(json_file)
    return data

# merge value to json
def merge_Value_2_Json(path_to_value, path_to_file_json):
  Values = open(path_to_value, 'r')
  Dict = ParJson2Dict(path_to_file_json)
  for obj in Dict['WaL0']:
    String = Values.readline()
    obj['fill_val'] = String[:-1]
  return Dict

# add arguments for file
import argparse
ap = argparse.ArgumentParser()
ap.add_argument('-m', '--mode', required=True, help='mode for working')
ap.add_argument('-u', '--user_value', required=True, help='Path to user file')
ap.add_argument('-it', '--input_template', required=True, help='Path to template json input')
ap.add_argument('-uj', '--user_json', required=True, help='Path to user json')

ap.add_argument('-f', '--file_name', required=True, help='Path to file name')
ap.add_argument('-p', '--position', required=True, help='Path to file position')
ap.add_argument('-ot', '--output_template', required=True, help='Path to template json output')

args = vars(ap.parse_args())


# save user json
if (args['mode']=='1'):
  Dict = merge_Value_2_Json(args['user_value'], args['input_template'])
  with open(args['user_json'], 'w') as outfile:
    json.dump(Dict, outfile)

# save template json
if (args['mode']=='2'):
  DictionaryCreate(args['file_name'], args['position'], args['output_template'])
