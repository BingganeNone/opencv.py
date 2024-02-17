import cv2 as cv


img = cv.imread('dog.jpg')
cv.imshow("Dog",img)
#cv.waitKey(0)
"""
capture = cv.VideoCapture("dog.mp4")
while True:
    isTrue,frame = capture.read()
    cv.imshow("Video",frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
cv.waitKey(0)
"""