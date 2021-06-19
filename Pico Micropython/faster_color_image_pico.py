import lcd_lib as lcd

# Provide Image File Name Here
image_name = 'test'

LCD = lcd.LCD_1inch3()
background = LCD.white
LCD.fill(background)
LCD.show()

f = open(image_name,'r')

row_count = 0

while True:
    data = f.readline()
    if not data:
        break
    px_ptr = 0
    # All Even Positions will be Pixel Counts and
    # all odd positions will be Pixel Color Values
    data = data.split(',')
    for i in range(len(data)):
        # Reading Count of Homogenous Pixels
        if i%2 == 0:
            px_count = int(data[i])
        # Reading the Color of the Homogenous Pixels
        else:
            color = int('0x'+data[i])
            for j in range(px_ptr,px_count+px_ptr):
                # Ignoring Pixels having save color as background
                if color == background:
                    break
                LCD.pixel(j,row_count,color)       
            px_ptr += px_count
            
    LCD.show()
    row_count += 1

