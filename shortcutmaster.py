# Shortcut Master for Raspberry Pi Version 1.1
# This is the main code for the program, it was designed by SC13NC3F1CT10N (username)
# Version code made 04/10/2020


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

# Edit these to change command <FUNCTION = "COMMAND:STRING">
func1 = "lxterminal -t ShortcutMaster" # Terminal
func2 = "/usr/bin/vlc --started-from-file %U" # VLC Media Player
func3 = "chromium-browser %U" # Chromium Web Browser
func4 = "pcmanfm" # File manager

def wunp(): # Create wunp (wait until not pushed) function
    while GPIO.input(10) == GPIO.HIGH:
        pass

sound = True # Set to False if you don't want sound or set to True if you want sound

def playsound(): # This function plays sound when sound is enabled.
    if sound == True:
        system("mpg123 /home/pi/ShortcutMaster_Raspberry-Pi/sounds/launch.mp3")
# Let the user know the program is ready to begin
GPIO.output(8, GPIO.HIGH)
print("Ready")

## MAIN ##
stop = False
while stop == False: # Run until stop = True
    # If button (1 to 4) is pushed, execute set command then stop the script
    if GPIO.input(10) == GPIO.HIGH:
        print("Execute: " + func1)
        playsound()
        system(func1)
        stop = True
        wunp()
    if GPIO.input(12) == GPIO.HIGH:
        print("Execute: " + func2)
        playsound()
        system(func2)
        stop = True
        wunp()
    if GPIO.input(16) == GPIO.HIGH:
        print("Execute: " + func3)
        playsound()
        system(func3)
        stop = True
        wunp()
    if GPIO.input(18) == GPIO.HIGH:
        print("Execute: " + func4)
        playsound()
        system(func4)
        stop = True
        wunp()
        
print("Goodbye")
