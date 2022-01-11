import cv2
CAM_ID = 0
#Open the CAM
cap = cv2.VideoCapture(CAM_ID) # 카메라 생성
# create the window & change the window size
# 윈도우 생성 및 사이즈 변경
cv2.namedWindow('Face')
face_cascade = cv2.CascadeClassifier()
# opencv 의 인식모듈을 사용하기위해 사용해야하는 라이브러리
face_cascade.load(r'./xml/haarcascade_frontalface_default.xml')
# opencv 설치후 해당 xml 의 경로를 자신의 컴퓨터에 맞도록 확인해야합니다
while(True):
    #read the camera image
    # 카메라에서 이미지 얻기
    ret, frame = cap.read()
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 회색으로 좀더 얼굴 인식 구별 확인 / 얼굴 인식이 안되면 0 , 되면 1
    grayframe = cv2.equalizeHist(grayframe)

    faces = face_cascade.detectMultiScale(grayframe , 1.1, 3, 0, (30,30))
    if faces is():
        print("1")
    else:
        print("0")
    # 얼굴에 사각형을 표시
    for (x,y,w,h ) in faces:
        cv2.rectangle(frame,(x,y), ( x+w,y+h),(0,255,0),3, 4,0)
        cv2.imshow("Face",frame)
        #10ms 동안 키입력 대기
        if cv2.waitKey(10) >= 0:
            break;
        #close the window
        # 윈도우 종료
cap.release
cv2.destroyWindow('Face')