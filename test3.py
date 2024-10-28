import cv2

img = cv2.imread('image.png')
img_rot = cv2.rotate(img, cv2.ROTATE_180)

cv2.imshow('CAT!',img)
cv2.imshow('what!', img_rot)


cv2.waitKey(0)
