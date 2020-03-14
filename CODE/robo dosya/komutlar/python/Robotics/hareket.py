import RPi.GPIO as gpio
import time
from mesafe import distance
aci = aci2 = aci3 = 6

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(27,gpio.OUT)
    gpio.setup(17,gpio.OUT)
    gpio.setup(18,gpio.OUT)
    gpio.setup(22,gpio.OUT)

def ileri(tf):
    init()
    gpio.output(22,1)
    gpio.output(18,1)
    gpio.output(17,0)
    gpio.output(27,0)
    time.sleep(tf)
    gpio.cleanup()

def geri(tf):
    init()
    gpio.output(17,1)
    gpio.output(27,1)
    gpio.output(22,0)
    gpio.output(18,0)
    time.sleep(tf)
    gpio.cleanup()

def sol(tf):
    init()
    gpio.output(18,1)
    gpio.output(27,1)
    gpio.output(22,0)
    gpio.output(17,0)
    time.sleep(tf)
    gpio.cleanup()

def sag(tf):
    init()
    gpio.output(22,1)
    gpio.output(17,1)
    gpio.output(18,0)
    gpio.output(27,0)
    time.sleep(tf)
    gpio.cleanup()

def dur():
    init()
    gpio.output(22,0)
    gpio.output(17,0)
    gpio.output(18,0)
    gpio.output(27,0)
    gpio.cleanup()

def servo(tf):
    gpio.setmode(gpio.BCM)
    gpio.setup(5,gpio.OUT)
    p = gpio.PWM(5,50)
    p.start(6)
    p.ChangeDutyCycle(tf)
    time.sleep(0.7)
    gpio.cleanup()    

def servo2(tf):
    gpio.setmode(gpio.BCM)
    gpio.setup(6,gpio.OUT)
    p2 = gpio.PWM(6,50)
    p2.start(6)
    p2.ChangeDutyCycle(tf)
    time.sleep(0.7)
    gpio.cleanup()

def servo3(tf):
    gpio.setmode(gpio.BCM)
    gpio.setup(20,gpio.OUT)
    p3 = gpio.PWM(20,50)
    p3.start(6)
    p3.ChangeDutyCycle(tf)
    time.sleep(0.7)
    gpio.cleanup()

print ("hosgeldiniz")
print ("          ")
time.sleep(1)
print ("komut karakterlerinin anlamlari:")
print ("w: ileri git")
print ("s: geri git")
print ("a: sola don")
print ("d: saga don")
print ("j: kafayi duz konuma getir")
print ("u: kafayi yukari kaldir")
print ("n: kafayi asagi indir")
print ("h: kafayi sola cevir")
print ("k: kafayi saga cevir")
print ("r: kancayi kaldir")
print ("f: kancayi indir")
print ("b: fren yap(dur)")
print ("c: programdan cikis")
print ("t: hayir ifadesi")
print ("y: evet ifadesi")
print ("g: uzgun ifade")
print ("        ")   
time.sleep(2)

while (True):
    dis = distance('cm')
    print 'mesafe',dis
    y = raw_input("komut karakteri:")
    time.sleep(0.03)
    if (y == "w"):
        print ("ileri")
        ileri(0.6)
    elif (y == "s"):
        print ("geri")
        geri(0.6)
    elif (y == "d"):
        print ("sag")
        sag(0.6)
    elif (y == "a"):
        print ("sol")
        sol(0.6)
    elif (y == "c"):
        print ("hoscakal")
        break
    elif (y == "j"):
        print ("duz bakiliyor aci = aci2 =6")
        servo(6)
        servo2(6)
        aci = 6
        aci2 = 6
    elif (y == "n"):
        aci2 = aci2 + 1
        print 'asagi bakiliyor,aci2 = ',aci2
        servo2(aci2)
    elif (y == "u"):
        aci2 = aci2 - 1
        print 'yukari bakiliyor,aci2 = ',aci2
        servo2(aci2)
    elif (y == "h"):
        aci = aci + 1
        print 'sola bakiliyor,aci = ',aci
        servo(aci)
    elif (y == "k"):
        aci = aci - 1
        print 'saga bakiliyor,aci = ',aci
        servo(aci)
    elif (y == "r"):
        aci3 = aci3 + 1
        print 'kanca yukari,aci = ',aci3
        servo3(aci3)
    elif (y == "f"):
        aci3 = aci3 - 1
        print 'kanca asagi,aci = ',aci3
        servo3(aci3)
    elif (y == "b"):
        print ("fren yapiliyor")
        dur()
    elif (y == "y"):
        print ("evet ifade ediliyor")
	servo2(6)
	servo2(5)
	servo2(6)
    elif (y == "t"):
	print ("hayir ifade ediliyor")
	servo(6)
	servo(5)
	servo(7)
	servo(6)
    elif (y == "g"):
	print ("  :(  ")
	servo2(6.6)
	servo(5.5)
	servo(6.5)
	servo(5.5)
	servo(6.5)
	servo(5.5)
	servo(6.5)
	servo2(6)
	servo(6)	
    else:
        print ("anlamadim tekrar dene")
        dur()
        pass
