import cv2 as cv

img_path_target = r"C:\Hong\drone_edu\D2\img\drone_target.png"
img_path_drones = r"C:\Hong\drone_edu\D2\img\7_drones.jpg"

# 여러사진이 있는 사진을 흑백으로 불러옵니다
drones_img_black = cv.imread(img_path_drones, 0)
img_target = cv.imread(img_path_target, 0)
# 컬러
drones_img_color = cv.imread(img_path_drones)

# 원하는 이미지를 특정화
result = cv.matchTemplate(drones_img_black, img_target, cv.TM_SQDIFF)

# 원하는 이미지의 위치 설정
minVal , maxVal , minLoc , maxLoc = cv.minMaxLoc(result)
x, y = minLoc
h,w = img_target.shape

# draw bbox on the image
# 원하는 이미지에 사각형 표시
drones_img_color = cv.rectangle(drones_img_color, (x, y), (x + w, y + h), (0,0,255), 2)

cv.imshow("result",drones_img_color)
cv.waitKey(0)
cv.destroyAllWindows()