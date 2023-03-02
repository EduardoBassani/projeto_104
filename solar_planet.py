import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Sol", (100,80), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale =0.6, color=(0,0,255))
cv2.putText(img, "Mercurio", (95,180), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale =0.6, color=(0,0,255))
cv2.putText(img, "Venus", (200,170), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale =0.6, color=(0,0,255))
cv2.putText(img, "Terra", (275,170), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale =0.6, color=(0,0,255))
cv2.putText(img, "Marte", (370,170), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale =0.6, color=(0,0,255))
cv2.putText(img, "Jupiter", (575,50), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale =0.6, color=(0,0,255))
cv2.putText(img, "Saturno", (750,110), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale =0.6, color=(0,0,255))
cv2.putText(img, "Urano", (975,130), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale =0.6, color=(0,0,255))
cv2.putText(img, "Neturno", (1075,130), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale =0.6, color=(0,0,255))

cv2.imwrite("solar-system.jpg", img)
cv2.imshow("resultado", img)
cv2.waitKey(0)
