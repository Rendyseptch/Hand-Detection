import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector()

while True:
    ret, frame = cap.read()
    if ret:
        hands, img_out = detector.findHands(frame)
        cv2.imshow('img_out', img_out)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()

