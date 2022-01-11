from time import sleep

from e_drone.drone import *
from e_drone.protocol import *



if __name__ == "__main__":
    drone = Drone()
    drone.open("COM3")

    red_on = 255
    red_off = 0
    green_on = 255
    green_0ff = 0
    blue_on = 255
    blue_0ff = 0

    print("Take Off!!")
    drone.sendTakeOff()
    sleep(0.01) # for 0.01 sec
    drone.sendLightDefaultColor(LightModeDrone.BodyDimming, 1, red_on, green_0ff, blue_0ff)
    sleep(0.05)

    print("Hovering!!")
    drone.sendLightDefaultColor(LightModeDrone.BodyDimming, 1, red_off, green_on, blue_0ff)
    sleep(0.05)
    drone.sendControlWhile(0, 0, 0, 0, 3000) # hover for 3 sec

    print("Go Stop!!")
    drone.sendLightDefaultColor(LightModeDrone.BodyDimming, 1, red_off, green_0ff, blue_on)
    sleep(0.05)
    drone.sendControlWhile(0, 0, 0, 0, 1000) # stay for 1 sec

    print("Landing!!")
    drone.sendLanding() # need to landing func twice only can stop
    sleep(0.01)
    drone.sendLanding() 
    sleep(0.01)

    drone.close()