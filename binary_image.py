# Use this file when the image to be displayed is binary
# i.e. is only black and white, eg: QR codes, Barcodes etc
# This implementation is faster than the colored image one
# Make sure that the image is *NOT* more than 250*250 Pixels

import cv2

# Provide your filename here
file_name = 'qr.png'
img = cv2.imread(file_name,0)
RES = img.shape[0]
file_name = file_name.split('.')[0]

string = ''

# Compression and Encoding Grayscale image
map = {}
for i, row in enumerate(img):
  start = []
  end = []
  for j, _ in enumerate(row):
      # First Black Pixel Capture
      if j<RES-1 and row[j] > 0 and row[j+1] == 0: 
        start.append(j+1)
      # Last Black Pixel Capture
      elif j<RES-1 and row[j] == 0 and row[j+1] > 0:
        end.append(j)

  if start or end:
    map[i] = list(zip(start,end))
    string += str(i) + ':'
    string += ','.join([str(item) for sublist in map[i] for item in sublist])
    string += '\n'


f = open(file_name, "w")
f.write(string)
f.close()


