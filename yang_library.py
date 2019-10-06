from gfxhat import lcd,backlight
import random
import time
# 1. function for displaying a vertical line on pi by a given x
def showVerticalLine(x):
    lcd.clear()
    y = 0
    while(y<=63):
        lcd.set_pixel(x,y,1)
        y += 1
    lcd.show()

# 2. function for displaying a horizontal line
def showHorizontalLine(y):
    lcd.clear()
    x = 0
    for x in range(0,128):
        lcd.set_pixel(x,y,1)
        x += 1
    lcd.show()

# 3.function that creates a staircase starting at a specific coordinate. One stair has a width of w and a height of h.
def showStaircase(x,y,w,h):
    lcd.clear()
    while(x <= 127 and y <=63):
        x1 = x + w
        y1 = y + h
        if x1 <= 127:
            while (x < x1):
                lcd.set_pixel(x,y,1)
                lcd.show()
                x += 1
        else:
            while(x <= 127):
                lcd.set_pixel(x,y,1)
                lcd.show()
                x += 1
            break
        if y1 <= 63:
            while(y < y1):
                lcd.set_pixel(x,y,1)
                lcd.show()
                y += 1
        else:
            while(y <= 63):
                lcd.set_pixel(x,y,1)
                lcd.show()
                y += 1
            break

# 4.function that displays random pixel on the screen for a given period of time specifies in seconds.
def showRandomPixel(t):
    lcd.clear()
    i = 0
    while(i < t):
        x = random.randint(0,127)
        y = random.randint(0,63)
        lcd.set_pixel(x,y,1)
        lcd.show()
        i += 1
        time.sleep(1)

# 5.function to reset the backlight color
def clearBacklight(r,g,b):
    backlight.set_all(r,g,b)
    backlight.show()