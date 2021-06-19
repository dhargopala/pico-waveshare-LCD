# This implenetation is useful for Color Images, Color quality will be
# lower on accout of the quality of this screen. For Black and White
# images binary_image.py file usage is recommeded

import cv2

RES = 240
# Provide your Image Name here, PNG images are recommended as JPEG images
# have compression noise that does not translate well for 16-Bit Images
file_name = 'test.png'
img = cv2.imread(file_name)

if img.shape[0] > RES and img.shape[1] > RES:
    img = cv2.resize(img,(RES,RES))
elif img.shape[0] > RES:
    img = cv2.resize(img,(RES,img.shape[1]))    
elif img.shape[1] > RES :
    img = cv2.resize(img,(img.shape[0],RES))
    

file_name = file_name.split('.')[0]

def rgb_hex565(rgb):
    ''' Args:
            rgb: tuple having B,G,R values in decimal format
            
        Returns:
            64K Hexadecial image color code as a string
    '''
            
    # BRG - 565 format - Waveshare LCD
    # Flipping BGR to RGB
    blue, green, red = rgb[0], rgb[1], rgb[2]
    return ("%0.4X" % ((int(blue / 255 * 31) << 11) | (int(red / 255 * 63) << 5) | (int(green / 255 * 31))))


string = []

for i in range(len(img)):
    for j in range(len(img[i])):
        string.append(rgb_hex565(img[i][j]))
    string.append('\n')

string = ''.join([char for char in string])
f = open(file_name, "w")
f.write(string)
f.close()
