import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LED_PIN = 18
LED_PIN2 = 6
SCLPin = 17
SDOPin = 4

HALF_BIT_TIME=0.001
CHARACTER_DELAY = 2
NUM_BITS = 16

GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(SCLPin, GPIO.OUT)
GPIO.setup(SDOPin, GPIO.IN)
GPIO.output(SCLPin, GPIO.HIGH)
time.sleep(HALF_BIT_TIME)
oldKey = 18
MAXKEY = 18

DUTYCYCLE = 0
DUTYCYCLE2 = 0
p = GPIO.PWM(LED_PIN, 60)
p2 = GPIO.PWM(LED_PIN2, 60)

try:
    while True:
        oldKey = 18
        print("Hit a button on the keypad")
        button = 1
        time.sleep(CHARACTER_DELAY)
        while button < MAXKEY:
            print_button = button
            if(print_button == MAXKEY):
                print_button = 1
            GPIO.output(SCLPin, GPIO.LOW)
            time.sleep(HALF_BIT_TIME)
            keyval = GPIO.input(SDOPin)
            if not keyval:
                pressed = True
                if(oldKey != button):
                    print(print_button)
                    GPIO.output(SCLPin, GPIO.HIGH)
                    time.sleep(HALF_BIT_TIME)
                    break
            GPIO.output(SCLPin, GPIO.HIGH)
            time.sleep(HALF_BIT_TIME)
            button += 1
            
        if(print_button == 1):
            print('Hello World!')
        elif(print_button == 2):
            print('The current date and time is: ')
            print(datetime.datetime.utcnow())
        elif(print_button == 3):
            print('The current time is: ')
            print(datetime.datetime.now().strftime('%H:%M:%S'))
        elif(print_button == 4):
            if DUTYCYLE > 0:
                print('White LED is already on!')
            else:
                print('Turning on WHITE LED!')
                DUTYCYCLE = 50
                p.start(DUTYCYCLE)
        elif(print_button == 5):
            if DUTYCYCLE == 0:
                print('White LED is already off!')
            else:
                print('Turning off white LED!')
                DUTYCYCLE = 0
                p.ChangeDutyCycle(DUTYCYCLE)
                p.stop
        elif(print_button == 6):
            if DUTYCYCLE == 0:
                print('Hit key 4 to turn on the white LED')
            else:
                print('Changing to 25% Brightness on white LED')
                DUTYCYCLE = 25
                p.ChangeDutyCycle(DUTYCYCLE)
        elif(print_button == 7):
            if DUTYCYCLE == 0:
                print('Hit key 4 to turn on white LED')
            else:
                print('Changing to 100% Brightness on white LED')
                DUTYCYCLE = 100
                p.ChangeDutyCycle(DUTYCYCLE)
        elif(print_button == 8):
            if DUTYCYCLE2 > 0:
                print('Red LED is already on!')
            else:
                print('Turning on red LED!')
                DUTYCYCLE2 = 50
                p2.start(DUTYCYCLE2)
        elif(print_button == 9):
            if DUTYCYCLE2 == 0:
                print('Red LED is already off!')
            else:
                print('Turning off red LED!')
                DUTYCYCLE2 = 0
                p2.ChangeDutyCycle(DUTYCYCLE2)
                p2.stop
        elif(print_button == 10):
            if DUTYCYCLE2 == 0:
                print('Hit key 8 to turn on red LED!')
            else:
                print('Changing to 25% Brightness on red LED!')
                DUTYCYCLE2 = 25
                p2.ChangeDutyCycle(DUTYCYCLE2)
        elif(print_button == 11):
            if DUTYCYCLE2 == 0:
                print('Hit key 8 to turn on red LED!')
            else:
                print('Changing to 100% Brightness on red LED!')
                DUTYCYCLE2 = 100
                p2.ChangeDutyCycle(DUTYCYCLE2)
        elif(print_button == 12):
            if (DUTYCYCLE > 0 or DUTYCYCLE2 > 0):
                print('One of the LEDs or both of them are currently on, please turn both of them off')
            else:
                DUTYCYCLE = 50
                DUTYCYCLE2 = 50
                print('Turning on both LEDs')
                p.start(DUTYCYCLE)
                p2.start(DUTYCYCLE2)
        elif(print_button == 13):
            if (DUTYCYCLE == 0 or DUTYCYCLE2 == 0):
                print('One of the LEDs or both of them are already off, please turn both of them on')
            else:
                DUTYCYCLE = 0
                DUTYCYCLE2 = 0
                print('Turning both LEDs off')
                p.ChangeDutyCycle(DUTYCYCLE)
                p.ChangeDutyCycle(DUTYCYCLE2)
                p.stop
        elif(print_button == 14):
            if (DUTYCYCLE == 0):
                print('White LED is currently off, please turn it on!')
            if (DUTYCYCLE2 == 0):
                print('Red LED is currently off, please turn it on!')
            if (DUTYCYCLE != 0 and DUTYCYCLE2 != 0):
                DUTYCYCLE = 25
                DUTYCYCLE2 = 25
                print('Changing brightness of both LEDs to 25%')
                p.ChangeDutyCycle(DUTYCYCLE)
                p2.ChangeDutyCycle(DUTYCYCLE2)
        elif(print_button == 15):
            if (DUTYCYCLE == 0):
                print('White LED is currently off, please turn it on')
            if (DUTYCYCLE2 == 0):
                print('Red LED is currently off, please turn it off')
            if (DUTYCYCLE != 0 and DUTYCYCLE2 != 0):
                DUTYCYCLE = 100
                DUTYCYCLE2 = 100
                print('Changing brightness of both LEDs to 100%')
                p.ChangeDutyCycle(DUTYCYCLE)
                p.ChangeDutyCycle(DUTYCYCLE2)
        elif (print_button == 16):
            print('Goodbye World!')
            break
        else:
            print('no button pressed')
            
        pressed = False
        
except KeyboardInterrupt:
    pass

p.stop
p2.stop
GPIO.cleanup()
