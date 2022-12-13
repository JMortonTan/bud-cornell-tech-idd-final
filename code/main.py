### REQUIRED LIBRARY ###
# pip3 install makeblock
########################
import numpy as np
import cv2
import sys
import random
from time import sleep
from makeblock import MegaPi,SerialPort

# Open Serial Connection
megapi = MegaPi.connect(SerialPort.connect("/dev/ttyAMA0"))

# Define Motors
motor1 = megapi.DCMotor(1,1)
motor2 = megapi.DCMotor(1,2)
motor3 = megapi.DCMotor(2,1)
motor4 = megapi.DCMotor(2,2)

# Define Addresses
A6 = 60
A7 = 61
A8 = 62
A9 = 63
A10= 64
A11= 65
A12= 66
A13= 67
A14= 68
A15= 69

# Setup LED
led = megapi.RGBLed()

# Define Facial Detection Model and Setup Webcam
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
webCam = False
cap = cv2.VideoCapture(0)

def water_check():
    print("Checking water level")
    if (A15):
        return True
    else:
        return False

def water_dance():
    print("Init water dance")

    # Bud spins in place (Complaining and doing a rain dance)
    motor1.run(-50)
    motor2.run(50)
    motor3.run(-50)
    motor4.run(50)
    return

def light_check():
    print("Checking for light level")
    # Check infrared front left and right
    if (A6 == True and A7 == True):
        return True
    else:
        return False

# BAD PROGRAMMING FIX
def light_seek():
    print("Init light seek")
    while (A6 == True and A7 == True):
        motor1.run(50)
        motor2.run(50)
        motor3.run(50)
        motor4.run(50)
        light_seek()
    while (A6 == True and A7 == False):
        motor1.run(50)
        motor2.run(0)
        motor3.run(50)
        motor4.run(0)
        light_seek()
    while (A6 == True and A7 == False):
        motor1.run(0)
        motor2.run(50)
        motor3.run(0)
        motor4.run(50)
        light_seek()
    return

def setup_camera():
    if(len(sys.argv)>1):
        try:
            print("I'll try to read your image");
            img = cv2.imread(sys.argv[1])
            if img is None:
                print("Failed to load image file:", sys.argv[1])
        except:
            print("Failed to load the image are you sure that:", sys.argv[1],"is a path to an image?")
    else:
        try:
            print("Trying to open the Webcam.")
            if cap is None or not cap.isOpened():
                raise("No camera")
            webCam = True
        except:
            img = cv2.imread("../data/test.jpg")
            print("Using default image.")

# CURRENTLY NEVER LEAVES THIS LOOP IF INITIATED
def human_recognize():
    print("Checking human face")
    setup_camera()
    while(True):
        if webCam:
            ret, img = cap.read()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

        if webCam:
            cv2.imshow('face-detection (press q to quit.)',img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cap.release()
                break
        else:
            break
    return

def human_hide():
    print("init hide from human")
    motor1.run(-50)
    motor2.run(-50)
    motor3.run(-50)
    motor4.run(-50)
    return

# Function for human follow?
# def human_follow():
#     return

def butt_scratch():
    print("Init butt scratch")

    # Instantiate and Define Pixels Array
    pixels = [0]*12
    
    # Lets make some colour
    j = 0
    f = 0
    k = 0
    pixels[t*3] = int(16 * (1 + math.sin(t / 2.0 + j / 4.0)))
    pixels[t*3+1] = int(16 * (1 + math.sin(t / 1.0 + f / 9.0 + 2.1)))
    pixels[t*3+2] = int(16 * (1 + math.sin(t / 3.0 + k / 14.0 + 4.2)))
    
    # Set colours
    led.set_colors(pixels,A10)
    led.set_colors(pixels,A11)
    return

# Give owner headache
def zoomies():
    motor1.run(50)
    motor2.run(50)
    motor3.run(50)
    motor4.run(50)
    sleep(1)
    motor1.run(0)
    motor2.run(0)
    motor3.run(0)
    motor4.run(0)
    return

def diceroll():
    value = random.randint(1,100)
    if (value < 3):
        return True
    else:
        return False


# Logical Loop
while (True):
    # Check if bud is having butt scratch
    if (A13 and A14):
        butt_scratch

    # Check if bud should cry for water
    if (not water_check):
        water_dance
    else:

        # Check if bud should seek light
        if (not light_check):
            light_seek

        # Pets gonna do what pets gonna do
        # Custom sleep?  Rocks back and forth?
        sleep(50000)

        # Do some random shit and knock things over.
        if (diceroll()):
            # Grief owner
            zoomies()

        # Once in a while pretend to care about humans.
        if (diceroll()):
            if (not human_recognize()):
                human_hide()
