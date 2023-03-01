import cv2 as cv
import numpy as np


class VideoCap:
    cap = None
    path = None
    hue=None

    def __init__(self, path) -> None:
        self.path = path
        self.cap = cv.VideoCapture(self.path)
        self.hue=0

    def getNumberOfFrames(self):
        return int(self.cap.get(cv.CAP_PROP_FRAME_COUNT))

    def getHue(self):
        noOfFrames=self.getNumberOfFrames()
        for i in range (0,noOfFrames):
                flag,frame=self.cap.read()
                hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
                self.hue+= + np.mean(hsv[:,:,0])
        
        self.hue=round(self.hue/noOfFrames,4)
        return self.hue


capt = VideoCap(r"E:\HMS\Coding\Media\darkvid.mp4")

print(capt.getHue())
