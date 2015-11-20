import wiringpi2
import time
import RPi.GPIO as GPIO

PWM = 105
PWM_HIGH = 105
PWM_LOW = 87

def servoStart():

    while(PWM != PWM_LOW):
        wiringpi2.pwmWrite(18,PWM)
        PWM -= 1
        time.sleep(0.05)

    time.sleep(0.8)

    while(PWM != PWM_HIGH):
        wiringpi2.pwmWrite(18,PWM)
        PWM += 1
        time.sleep(0.06)

    wiringpi2.pwmWrite(18,PWM)


if __name__ == "__main__":
    servoStart()
