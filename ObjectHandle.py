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

# save image
# DictionaryCreate('./crop_image/field_name.txt', './WaL0.txt', './WaL0.json')

import json
# parse json to dictionary
def ParJson2Dict(path_to_file_json):
  with open(path_to_file_json) as json_file:
    data = json.load(json_file)
    return data
