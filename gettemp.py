#!/usr/bin/env python3
import RPi.GPIO as GPIO
import dht11
# import time
# import datetime
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

def gettemp():
    # initialize GPIO

    # read data using pin 4
    instance = dht11.DHT11(pin=4)

    result = instance.read()
    if result.is_valid():
        keys = ["Temperature", "Humidity"]
        values = [result.temperature, result.humidity]
        # print("Last valid input: " + str(datetime.datetime.now()))
        # print("Temperature: %d C" % result.temperature)
        # print("Humidity: %d %%" % result.humidity)
        return dict(zip(keys, values))

if __name__ == "__main__":
    gettemp()
