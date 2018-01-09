import RPi.GPIO as GPIO,time,os

GPIO.setmode(GPIO.BOARD)



def RCtime(RCpin):
    reading=0
    
    GPIO.setup(RCpin,GPIO.OUT)
    GPIO.output(RCpin,GPIO.LOW)
    time.sleep(.1)
    
    GPIO.setup(RCpin,GPIO.IN)
    while (GPIO.input(RCpin)== GPIO.LOW):
        reading+=1
    return reading

def dist():
    TRIG=38
    ECHO=40

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

    GPIO.output(TRIG,False)
    time.sleep(3)

    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)

    while GPIO.input(ECHO)==0:
        pulse_start=time.time()
    while GPIO.input(ECHO)==1:
        pulse_end=time.time()

    pulse_duration=pulse_end-pulse_start
    distance = pulse_duration*17150
    distance=round(distance,2)
    print distance
    return distance

count=0
temp=0
while True:
    x=RCtime(12)
    y=dist()
    print RCtime(12)
    if y< 50:
        
        if(RCtime(12) < 5000):
            print "nested if "          #Turn off bulb   
            GPIO.setup(11,GPIO.OUT)
            GPIO.output(11,GPIO.LOW)
            temp=0
        else:
            GPIO.setup(11,GPIO.OUT)
            if temp==0:
                print "nested nested if "          #Turn on bulb
                GPIO.output(11,GPIO.HIGH)
                temp=1
            else:
                print "nested nested else "
                GPIO.output(11,GPIO.LOW)             #Turn off bulb
                temp=0