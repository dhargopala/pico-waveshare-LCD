import lcd_lib as lcd

# Provide Image File Name Here
image_name = 'test'

LCD = lcd.LCD_1inch3()

LCD.fill(LCD.white)

line_no = 0

f = open(image_name,'r')

while True:
    data = f.readline()
    if not data:
        break
    hexvals = [int('0x'+data[n:n+4]) for n in range(0, len(data)-2, 4)]

    for pix ,color in enumerate(hexvals):
        LCD.pixel(pix, line_no, color)
    LCD.show()
        
    line_no += 1


