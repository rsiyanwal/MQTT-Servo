#!/usr/bin/python

# -- Importing the Libraries --
import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO
import random
import os

# -- Configurations --
MQTT_ADD = "Device's IP Address"
MQTT_USR = "Device's Name"
MQTT_PAS = "Device's Pass"
MQTT_TOP = "MQTT Topic"

# Setting the GPIO Pin numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output and set servo as pin 11 PWM
GPIO.setup(11, GPIO.OUT)
servo = GPIO.PWM(11, 50) # Pin 11, 50 Hz pulse

# Start PWM running, but with pulse off (value = 0)
servo.start(0)

# Angles
angles = [0, 90, 180]

# -- Connecting and Call Backs --
def on_connect (client, userdata, flags, rc):
    """ The Callback when the cloent receives a CONNACK response from the Server """
    print("Connected with Result Code " + str(rc))
    client.subscribe(MQTT_TOP)

def on_message(client, userdata, msg):
    """ The Callback when the PUBLISHED message is received from the Server """
    print(msg.topic + ": " + str(msg.payload))
    
    # Rotating Left
    if str(msg.payload) == "b'L'":
        ang = angles[0]
        print("Angle is: ", ang)
        servo.ChangeDutyCycle(2 + (ang/18))
        time.sleep(0.5)
        servo.ChangeDutyCycle(0)
        print(os.system("bash.sh"))
        
    # Rotating Center
    if str(msg.payload) == "b'C'":
        ang = angles[1]
        print("Angle is: ", ang)
        servo.ChangeDutyCycle(2 + (ang/18))
        time.sleep(0.5)
        servo.ChangeDutyCycle(0)
        # Executing Bash Command to take and image and save it
        print(os.system("bash.sh"))
    
    # Rotating Right
    if str(msg.payload) == "b'R'":
        ang = angles[2]
        print("Angle is: ", ang)
        servo.ChangeDutyCycle(2 + (ang/18))
        time.sleep(0.5)
        servo.ChangeDutyCycle(0)
        print(os.system("bash.sh"))
    
def main():
    mqtt_client = mqtt.Client();
    mqtt_client.username_pw_set(MQTT_USR, MQTT_PAS)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect(MQTT_ADD, 1883)
    mqtt_client.loop_forever()
    
    
if __name__ == '__main__':
    print("MQTT")
    main()
