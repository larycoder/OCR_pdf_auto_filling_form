# Get field name from cropped img

from tesserocr import PyTessBaseAPI
from tesserocr import PSM
import argparse
import glob


ap = argparse.ArgumentParser()
ap.add_argument('-d', '--directory', required=True, help='Path to image directory')
ap.add_argument('-o', '--output', required=True, help='Name of output txt file')

args = vars(ap.parse_args())

text = open(args['output'], 'w')
files = sorted(glob.glob(args['directory'] + '/*.jpg'))
print(files)
with PyTessBaseAPI(path = 'tesserocr/tessdata', lang='eng', psm=PSM.AUTO_OSD) as api:
    for file in files:
        api.SetImageFile(file)
        line = api.GetUTF8Text()
        print(text)
        text.write(line)
text.close()
