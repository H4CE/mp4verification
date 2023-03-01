import cv2 as cv
import numpy as np


class VideoCap:
    cap = None
    path = None
    contrast=None

    def __init__(self, path) -> None:
        self.path = path
        self.cap = cv.VideoCapture(self.path)
        self.contrast=0

    def getNumberOfFrames(self):
        return int(self.cap.get(cv.CAP_PROP_FRAME_COUNT))

    def getContrast(self):
        noOfFrames=self.getNumberOfFrames()
        for i in range (0,noOfFrames):
                flag,frame=self.cap.read()
                gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                self.contrast+=np.std(gray)
        
        self.contrast=round((self.contrast/noOfFrames),4)
        return self.contrast


capt = VideoCap(r"E:\HMS\Coding\Media\blackVid.mp4")

print(capt.getContrast())
