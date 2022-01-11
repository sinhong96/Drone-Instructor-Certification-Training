from time import sleep
from e_drone.drone import *
from e_drone.protocol import *
def eventMotion(motion):
    print("eventMotion()")
    print("- Accel (X, Y, Z): {0:5}, {1:5}, {2:5}".format(motion.accelX, motion.accelY, motion.accelZ))
    print("- Gyro (Roll, Pitch, Yaw): {0:5}, {1:5}, {2:5}".format(motion.gyroRoll, motion.gyroPitch, motion.gyroYaw))
    print("- Angle (Roll, Pitch, Yaw): {0:5}, {1:5}, {2:5}".format(motion.angleRoll, motion.anglePitch, motion.angleYaw))
if __name__ == '__main__':
    drone = Drone()
    drone.open("COM3")
    # 이벤트 핸들링 함수 등록
    drone.setEventHandler(DataType.Motion, eventMotion)
    while True:
        # Range 정보 요청
        drone.sendRequest(DeviceType.Drone, DataType.Motion)
        sleep(1)
        drone.close()