# Shortcut Master for Raspberry Pi Version 1.0
# This is the main code for the program, it was designed by SC13NC3F1CT10N (username)
# Version code started 04/09/2020 and ended 04/10/2020


## SETUP ##
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO module as GPIO
from os import system # Import the system function from os module
GPIO.setwarnings(False) # Ignore warnings
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Setup pin 10 as an input pin and set initial value to be pulled low (off) 
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Setup pin 14 as an input pin and set initial value to be pulled low (off)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Setup pin 16 as an input pin and set initial value to be pulled low (off) 
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Setup pin 18 as an input pin and set initial value to be pulled low (off) 
GPIO.setup(8, GPIO.OUT, initial = GPIO.LOW) # Setup pin 14 as an input pin and set initial value to be pulled low (off) 

# Edit these to change command (FUNCTION = "COMMAND:STRING")
func1 = "lxterminal -t ShortcutMaster"
func2 = "minecraft-pi"
func3 = "chromium-browser %U"
func4 = "pcmanfm"

def wunp(): # Create wunp (wait until not pushed) function
    while GPIO.input(10) == GPIO.HIGH:
        pass

# Let the user know the program is ready to begin
GPIO.output(8, GPIO.HIGH)
print("Ready")

## MAIN ##
stop = False
while stop == False: # Run until stop = True
    # If button (1 to 4) is pushed, execute set command then stop the script
    if GPIO.input(10) == GPIO.HIGH:
        print("Execute: " + func1)
        system(func1)
        stop = True
        wunp()
    if GPIO.input(12) == GPIO.HIGH:
        print("Execute: " + func2)
        system(func2)
        stop = True
        wunp()
    if GPIO.input(16) == GPIO.HIGH:
        print("Execute: " + func3)
        system(func3)
        stop = True
        wunp()
    if GPIO.input(18) == GPIO.HIGH:
        print("Execute: " + func4)
        system(func4)
        stop = True
        wunp()
print("Goodbye")
