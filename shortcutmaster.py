## SETUP ##

# Import needed modules
from gpiozero import Button
from time import sleep
from os import system
from signal import pause
import RPi.GPIO as GPIO
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

# Set up lcd rows and columns
lcd_columns = 16
lcd_rows = 2

lcd_rs = digitalio.DigitalInOut(board.D22)
lcd_en = digitalio.DigitalInOut(board.D17)
lcd_d4 = digitalio.DigitalInOut(board.D25)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d6 = digitalio.DigitalInOut(board.D23)
lcd_d7 = digitalio.DigitalInOut(board.D18)


# Create lcd class
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                      lcd_d7, lcd_columns, lcd_rows)
# Create waituntil() function
def waituntil(action):
    while not action:
        pass
# Tell user project is loading
lcd.message = "LOADING..."
    
## MAIN ##
try:
    GPIO.setmode(GPIO.BCM) # Use physical pin numbering
    GPIO.setwarnings(True) # Ignore warning for now
    # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(32, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    # Launch terminal when button pushed

    sleep(1)
    while True: # Run forever
        lcd.clear()
        lcd.message = "Awaiting Button"
        sleep(1)
        if GPIO.input(32) == GPIO.HIGH:
            print(":(")
            lcd.clear()
            lcd.message = "Launched Item"
            sleep(0)  
except:
    RuntimeError("The GPIO channel has not been set up as an OUTPUT")
    lcd.message = "Error"
