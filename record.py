import cv2
import numpy as np
import pyautogui


def record():
    img = pyautogui.screenshot()
    frame=cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    return frame


def display(frame):
    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
    # cv2.resizeWindow("Live", 480, 270)
    cv2.imshow('Live', frame)


while True:
    display(record())
    if cv2.waitKey(1) == ord('q'):
        break