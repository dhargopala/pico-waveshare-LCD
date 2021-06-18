import lcd_lib as lcd

file_name = 'qr'

LCD = lcd.LCD_1inch3()

file = open(file_name, "r")

LCD.fill(LCD.white)

data = file.read()
data = data.split('\r\n')

for line in data:
    row, elements = line.split(':')
    elements = elements.split(',')
    for i in range(0,len(elements),2):
        for k in range(int(elements[i]),int(elements[i+1])+1):
            LCD.pixel(int(row), k, LCD.black)
            
    LCD.show()


    
        



  
    


