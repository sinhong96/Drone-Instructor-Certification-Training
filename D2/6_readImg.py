import cv2 as cv

img_path = "C:\Hong\drone_edu\D2\img\codrone.jpg"
img = cv.imread(img_path)
#경로에 있는 이미지를 불러오고 뒤에 0 을 입력하면 흑백이 됩니다
print(img.shape) 
# 이미지의 사이즈가 반환됨

# cv.imshow("window_title", img) # 이미지를 실행시킴

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#이미지를 흑백으로 바꾸어줍니다

cv.imshow("window_title",img_gray)
cv.waitKey(0)
