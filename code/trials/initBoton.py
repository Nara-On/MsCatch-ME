import RPi.GPIO as GPIO

# 4	LED
# 22  BUTTON
BUTTON_PIN = 15

def button_callback(channel):
    print("Button was pushed!")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(BUTTON_PIN, GPIO.RISING, callback=button_callback) # Setup event on pin 10 rising edge

message = input("Press enter to quit\n\n") # Run until someone presses enter

# while True:
#     if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
#         print("button was pressed")
#         break



GPIO.cleanup() # Clean up
