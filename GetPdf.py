import img2pdf
import argparse
import os
import io

ap = argparse.ArgumentParser()
ap.add_argument('-d', '--directory', required=True, help='path to folder contains images')
ap.add_argument('-o', '--output', required=True, help='output pdf file')
args = vars(ap.parse_args())

bytesIOs = []
for img in os.listdir(args['directory']):
  if img.endswith('.jpg'):
    with open(args['directory'] + '/' + img, 'rb') as f:
      bytesIOs.append(io.BytesIO(f.read()))

with open(args['output'], 'wb') as o:
  o.write(img2pdf.convert([i.read() for i in bytesIOs]))

