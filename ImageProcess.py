# rescale percent
per_cent = 35

# convert pdf to jpg
from pdf2image import convert_from_path
def convertPdf2Jpg(path_to_file):
  pages = convert_from_path(path_to_file)
  count = 0
  for page in pages:
    string = path_to_file[:3] + str(count) + '.jpg'
    print(string)
    page.save(string, 'JPEG')
    count = count + 1

# extract Dimension of String
def extract_String_2_Dimension(line):
  line = line.replace('(','')
  line = line.replace(')','')
  line = line[1:-2].split(',')
  for index, x in enumerate(line):
    line[index] = float(x)
  (x1, y1, x2, y2) = line
  x1 = int((x1 * 100) / per_cent)
  x2 = int((x2 * 100) / per_cent)
  y1 = int((y1 * 100) / per_cent)
  y2 = int((y2 * 100) / per_cent)
  return (x1, y1, x2, y2)

# crop image function
import cv2
def cutImage(path_to_image, path_to_file, path_to_save):
  # load image and coodinates 
  img = cv2.imread(path_to_image)
  file = open(path_to_file,'r')
  # crop image following dimensions break with Esc key
  count = 0
  for line in file:
    line = line.replace('(','')
    line = line.replace(')','')
    line = line[1:-2].split(',')
    for index, x in enumerate(line):
      line[index] = int(x)
    (x1, y1, x2, y2) = line
    x1 = int((x1 * 100) / per_cent)
    x2 = int((x2 * 100) / per_cent)
    y1 = int((y1 * 100) / per_cent)
    y2 = int((y2 * 100) / per_cent)
    crop_img = img[y1:y2, x1:x2]
    if (count % 2) == 0:
      cv2.imwrite(path_to_save+'/'+'test'+('%03d'%(count/2))+'.jpg',crop_img)
    count = count + 1 
    k = cv2.waitKey(0)
    if k == 27:
      break
  file.close()


cutImage('templates/SOK/SOK2/SOK2.jpg', 'templates/SOK/SOK2/SOK2_rect_pos.txt','templates/SOK/SOK2/field')
# convertPdf2Jpg('SOKA.pdf')