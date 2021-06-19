# pico-waveshare-LCD
## This repository contains code that can be used to interface Waveshare LCD Hat (1.3") for Raspberry Pi Pico

The Pico has memory constraint of 256K, which means most color images cannot be directly displayed on any screen conneted to it.
If we try to load the whole image in memory, we get an out of memory error, as the Pico does not have enough memory to allocate.
In this code, instead of reading the whole image and storing it in memory of Pico, I've read the image line-by-line and updated the relevant pixels on screen,
such that the memory consumption is minimal. This however makes the image display step a bit slower, but it works nonetheless.

**NOTE: Copy the files in "Pico Micropython directory" to the Raspberry Pi Pico**

## For Binary Images
* Paste the binary image (eg: QR Code, Barcode) in the same directory on your local machine
* In binary_image.py change file_name variable to the name of the image
* Run the python file
* Either copy the newly generated file directly to the Pico or copy the contents of this file to a new file in Pico and save it
* Open the binary_image_pico.py file and change the file_name to the name of newly pasted file
* Run binary_image_pico.py

## For Color Images
* Paste the color image in the same directory on your local machine
* In img2img565.py change file_name variable to the name of the image
* Run the python file
* Either copy the newly generated file directly to the Pico or copy the contents of this file to a new file in Pico and save it
* Open the colour_image_pico.py file and change the file_name to the name of newly pasted file
* Run colour_image_pico.py

Do note that binary_image_pico.py file runs faster for the Binary files as compared to colour_image_pico.py file due to the nature of the encoding used for binary files
