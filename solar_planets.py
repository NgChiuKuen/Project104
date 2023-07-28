import cv2

img = cv2.imread("solar-system.jpg")
# cv2.imshow("output", img)


# Add text below each planet

# cv2.putText(img, "Mercury", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
# cv2.putText(img, "Venus", (150, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
# cv2.putText(img, "Earth", (250, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
# cv2.putText(img, "Mars", (350, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
# cv2.putText(img, "Jupiter", (450, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
# cv2.putText(img, "Saturn", (550, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
# cv2.putText(img, "Uranus", (650, 650), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
# cv2.putText(img, "Neptune", (750, 750), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.putText(img, "Sun", (50,400), cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 255))
cv2.putText(img, "Mercury", (95,400), cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 255))
cv2.putText(img, "Venus", (200,400), cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 255))
cv2.putText(img, "Earth", (275,400), cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 255))
cv2.putText(img, "Mars", (350,400), cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 255))
cv2.putText(img, "Jupiter", (410,400), cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 255))
cv2.putText(img, "Saturn", (515,400), cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 255))
cv2.putText(img, "Uranus", (605,400), cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 255))
cv2.putText(img, "Neptune", (695,400), cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 255))

cv2.imshow("Output", img)
cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg", img)