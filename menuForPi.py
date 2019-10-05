# a program showing a menu for user to chose pi function
from yang_library import clearBacklight, showHorizontalLine, showVerticalLine, showStaircase, showRandomPixel
print("which function do you want to use on raspberrypi?\n1.set backlight\n2.show a horizontal line on the screen\n3.show a vertical line on the screen\n4.show a staircase\n5.show some random pixel ")
option = int(input("Please enter the number of your option: "))
if option == 1:
    redValue = int(input("give a red value for rgb: "))
    greenValue = int(input("give a green value for rgb: "))
    blueValue = int(input("give a blue value for rgb: "))
    clearBacklight(redValue,greenValue,blueValue)
elif option == 2:
    yInput = int(input("input a value for y: "))
    showHorizontalLine(yInput)
elif option == 3:
    xInput = int(input("input a value for x: "))
    showVerticalLine(xInput)
elif option == 4:
    xPixel = int(input("input a value for x: "))
    yPixel = int(input("input a value for y: "))
    width = int(input("input a value for width: "))
    height = int(input("input a value for height: "))
    showStaircase(xPixel,yPixel,width,height)
elif option == 5:
    timeSec = int(input("input a time in second: "))
    showRandomPixel(timeSec)
                    

        