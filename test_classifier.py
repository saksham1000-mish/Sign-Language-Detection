import cv2
import mediapipe as mp

cap=cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)


while True:
    ret, frame=cap.read()

    cv2.imshow('frame', frame)
    cv2.waitKey(25)
cap.release()
cv2.destroyAllWindows()

