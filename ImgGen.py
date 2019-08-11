import json
import cv2 as cv
import img2pdf
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-t', '--template', required=True, help='Path to json file')
ap.add_argument('-o', '--output', required=True, help='Name of output JPG file')
ap.add_argument('-i', '--input', required=True, help='Name of input image')
args = vars(ap.parse_args())

def ParJson2Dict(path_to_file_json):
  with open(path_to_file_json) as json_file:
    data = json.load(json_file)
    return data
  
def write_text(img, matrix, text):
  (x1,y1,x2,y2)=matrix
  location = (min(x1, x2), max(y1, y2))
  cv.putText(img, text, location, cv.FONT_HERSHEY_PLAIN, 1.25, (0, 0, 0), 1)
  
jsonFile = args['template']
imgPath = args['input']
imgPathOut = args['output']

Dict = ParJson2Dict(jsonFile)

img = cv.imread(imgPath)

for pos in Dict['WaL0']:
  x1 = pos['fill_pos']['x1']
  x2 = pos['fill_pos']['x2']
  y1 = pos['fill_pos']['y1']
  y2 = pos['fill_pos']['y2']
  write_text(img, (x1, y1, x2, y2), pos['fill_val'])

cv.imwrite(imgPathOut, img)