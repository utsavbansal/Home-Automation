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
    time.sleep(.2)

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
    print distance," cm"
    return distance

count=0
bulb_on=0
while True:
    x=RCtime(12)
    y=dist()
    print RCtime(12)
    if RCtime(12) > 5000:
        
        #if y< 50 and count>0 and bulb_on==1:
         #   count-=1
          #  GPIO.setup(11,GPIO.OUT)
           # GPIO.output(11,GPIO.LOW)  #turn off
            #bulb_on=0
        if y<55 and y>0 and bulb_on==0:
            count+=1
            GPIO.setup(11,GPIO.OUT)  # turn on
            GPIO.output(11,GPIO.HIGH)
            bulb_on=1
            print "Bulb on"
            
    elif RCtime(12) < 5000 and RCtime(12) > 0 :
        if y < 55 and y>0  and bulb_on==1:
            count-=1
            GPIO.setup(11,GPIO.OUT)
            GPIO.output(11,GPIO.LOW)  #turn off
            print "Bulb off"
            bulb_on=0
            