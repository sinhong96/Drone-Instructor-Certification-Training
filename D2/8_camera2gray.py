import numpy as np
import cv2

# 0 은 cam 의 id 로 여러개 있으면 0,1,2 로 고유 id 가 생깁니다
cap = cv2.VideoCapture(0)

cap.set(3,640) # set Width # 영상 가로 넓이 설정
cap.set(4,480) # set Height # 영상 세로 높이 설정
while(True):
#while(cap.isOpened()):
    ret, frame = cap.read()

    # Flip camera vertically # 영상 상하반전유무에 따라 0,1 을 사용
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 영상처리를 위한 흑백처리
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()