import smbus
import time

BH1750_sensor = 0x23

# represent 0 if power is off
turnoff = 0x00

# represent 1 if power is on
turnon = 0x01

# reset the whole setup
Reset = 0x07

recieved_address = 0x23

bus = smbus.SMBus(1)

def Light():
    address = bus.read_i2c_block_data(BH1750_sensor,recieved_address)
    value = Light_intensity(address)
    return value

def Light_intensity(address): 
    result=((address[1] + (256 * address[0]))/1.2)
    return result

def message():
    while True:
        intensity = Light()
        print(Light())
        if(intensity>= 500):
            print("Too Bright")
        elif(intensity> 200 and intensity<500):
            print("Bright")
        elif(intensity > 50 and intensity< 200):
            print("Medium")
        elif(intensity<50 and intensity>20):
            print("Dark")
        elif(intensity<20):
            print("Too Dark")
        time.sleep(1)

message()
