import cv2 as cv
import numpy as np


class VideoCap:
    cap = None
    path = None
    noOfFrames = None

    def __init__(self, path) -> None:
        self.path = path
        self.cap = cv.VideoCapture(self.path)
        self.noOfFrames = int(self.cap.get(cv.CAP_PROP_FRAME_COUNT))

    def getNumberOfFrames(self):
        return int(self.cap.get(cv.CAP_PROP_FRAME_COUNT))
        
    def getBrightnessOfVideo(self):

        brigthness = 0
        noOfFrames = self.getNumberOfFrames()

        for i in range(0, noOfFrames):
            
            flag, frame = self.cap.read()
            hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            brigthness +=np.mean(hsv[:, :, 2])

        brigthness = round(brigthness /(noOfFrames), 4)
        return brigthness


capt = VideoCap(r"E:\HMS\Coding\Media\whiteVid.mp4")

print(capt.getBrightnessOfVideo())

