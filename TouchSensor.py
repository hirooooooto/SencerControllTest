import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.IN)


def JudgeTouchSensor():

    while(True):
        inputValue = GPIO.input(12)

        if(inputValue == True):
            print("Touch Success")
        else:
            print("Touch failure")

        time.sleep(1)


if __name__ == "__main__":
    JudgeTouchSensor()
