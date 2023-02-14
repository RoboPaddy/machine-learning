import RPi.GPIO as GPIO

 
 
def setup():
	# set: never output warnings
	GPIO.setwarnings(False)
	# set gpio mode to bcm
	GPIO.setmode(GPIO.BCM)
	# set control pin to gpio22
	global trig 
	trig=22
	# set receive pin to gpio17
	global echo 
	echo=17 #receive-pin
	# set control pin to output mode, initialise output as low level
	GPIO.setup(trig,GPIO.OUT,initial=GPIO.LOW)
	# set receive pin to input mode
	GPIO.setup(echo,GPIO.IN)
 
 
def Measure(time):
    # set control pin to high level
    GPIO.output(trig,True)
    #delay 1us
    #time.sleep(0.0001)
    try:
        time.sleep(0.0001)
    except:
        time.sleep = 0.0001
    # set control pin to low level
    GPIO.output(trig,False)
 
    # used to measure time, continue looping waiting for the receive pin to become 0
    while GPIO.input(echo)==0:
        pass
    # input value becomes 0, start to measure time, record current time to start
    start=time.time()
 
    # looping waiting for receive pin to become 1
    while GPIO.input(echo)==1:
        pass
    # input value becomes 1, stop measuring time, record current time to end
    end=time.time()
 
 
 
    # measure distance
    distance=round((end-start)*343/2*100,2)
    return distance
    #print("distance:{0}cm,{1}m".format(distance,distance/100))
 
    
 
 
# loop to measure distance，sleep every 1s
'''
while True:
    Measure()
    time.sleep(1)
 
GPIO.cleanup();
'''
