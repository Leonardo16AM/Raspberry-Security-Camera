import cv2
import numpy as np
from datetime import datetime

def resize_frame(frame, scale_percent):
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

def detect_motion(video_source=0, save_path="/path/to/save/", scale_percent=50):
    cap = cv2.VideoCapture(video_source)
    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    frame1 = resize_frame(frame1, scale_percent)
    frame2 = resize_frame(frame2, scale_percent)

    while cap.isOpened():
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) < 500:
                continue

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            cv2.imwrite(f"{save_path}{timestamp}.jpg", frame1)
            break

        frame1 = frame2
        ret, frame2 = cap.read()
        frame2 = resize_frame(frame2, scale_percent)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_motion(video_source=0, save_path="/path/to/save/", scale_percent=50)
