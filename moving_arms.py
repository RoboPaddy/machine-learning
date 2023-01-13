# 0: head
# 1: left arm
# 2: right arm
# 3: left leg
# 4: right leg

from adafruit_servokit import ServoKit



def waving_arms(sleep): 
    kit=ServoKit(channels=16)
    servo=16 
    i = 0
    while i<5:
        # left arm
        kit.servo[1].angle = 0
        # right arm
        kit.servo[2].angle = 180
        # sleep for 1 second
        #sleep = 1
        sleep(1)

        kit.servo[1].angle = 180
        kit.servo[2].angle = 0

        i = i + 1

        #sleep = 1
        sleep(1)    	
if __name__ == "__main__":
    waving_arms()
