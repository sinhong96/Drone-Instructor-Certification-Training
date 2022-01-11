from time import sleep
from e_drone.drone import *
from e_drone.protocol import *
if __name__ == '__main__':
    drone = Drone()
    drone.open("COM3")

    print("TakeOff")
    drone.sendTakeOff()
    sleep(0.01)
    for i in range(3, 0, -1): #start, end, interval
        print("{0}".format(i)) # 0 is to print one dp digit
        sleep(1)
    
    print("Hovering")
    for i in range(1, 0, -1): #start, end, interval
        print("{0}".format(i))  # 0 is to print one dp digit
        drone.sendControlWhile(0, 0, 0, 0, 1000)
        sleep(1)