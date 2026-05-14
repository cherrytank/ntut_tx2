import cv2


CAMERA_ID = 0

cap = cv2.VideoCapture(CAMERA_ID)

if not cap.isOpened():
    print("Cannot open camera")
    raise SystemExit(1)

try:
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Cannot receive frame")
            break

        cv2.imshow("Webcam", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
