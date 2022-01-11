
import random
from time import sleep

from e_drone.drone import *
from e_drone.protocol import *

if __name__ == "__main__":

    drone = Drone(True, True, True, True, True)
    drone.open("COM3") # follow own com

    red_on = 255
    red_off = 0
    green_on = 255
    green_0ff = 0
    blue_on = 255
    blue_0ff = 0

    while True:
        drone.sendLightDefaultColor(LightModeDrone.BodyDimming, 1, red_on, green_0ff, blue_0ff)
        sleep(2)
        drone.sendLightDefaultColor(LightModeDrone.BodyDimming, 1, red_off, green_on, blue_0ff)
        sleep(2)
        drone.sendLightDefaultColor(LightModeDrone.BodyDimming, 1, red_off, green_0ff, blue_on)
        sleep(2)
        drone.close()
