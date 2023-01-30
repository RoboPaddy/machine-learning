import RPi.GPIO as GPIO

 
 
def setup():
	#设置警告信息为不输出
	GPIO.setwarnings(False)
	#设置gpio模式为bcm模式
	GPIO.setmode(GPIO.BCM)
	#控制引脚gpio22
	global trig 
	trig=22
	#接收引脚gpio17
	global echo 
	echo=17 #receive-pin
	#设置控制引脚为输出模式，初始化输出为低电平
	GPIO.setup(trig,GPIO.OUT,initial=GPIO.LOW)
	#设置接收引脚为输入模式
	GPIO.setup(echo,GPIO.IN)
 
 
#测量函数
def Measure(time):
    #将控制引脚设置为高电平
    GPIO.output(trig,True)
    #延时1us
    #time.sleep(0.0001)
    try:
        time.sleep(0.0001)
    except:
        time.sleep = 0.0001
    #将控制引脚设置为低电平
    GPIO.output(trig,False)
 
    #开始计算时间，在循环等待接收引脚的值变为0
    while GPIO.input(echo)==0:
        pass
    #输入变为0，开始计时，将当前时间保存到start
    start=time.time()
 
 
    #循环等待接收引脚变为1,
    while GPIO.input(echo)==1:
        pass
    #输入变为1，结束计时，将将当前时间保存到end
    end=time.time()
 
 
 
    #计算距离
    distance=round((end-start)*343/2*100,2)
    #控制台打印距离
    return distance
    #print("distance:{0}cm,{1}m".format(distance,distance/100))
 
    
 
 
#循环测量距离，间隔1s
'''
while True:
    Measure()
    time.sleep(1)
 
GPIO.cleanup();
'''
