import cv2 as cv


class VideoCap:
    cap = None
    path = None
    
    def __init__(self,path) -> None:
        self.path = path
        self.cap = cv.VideoCapture(self.path)

    def getFPS(self):
        return int((self.cap).get(cv.CAP_PROP_FPS))

    def getNumberOfFrames(self):
        return int(self.cap.get(cv.CAP_PROP_FRAME_COUNT))

    def getVideoLength(self):
        fps = self.getFPS()
        frameCount = self.getNumberOfFrames()   
        videoLength = frameCount // fps
        return videoLength


capt = VideoCap(f"E:\HMS\Coding\Media\darkvid.mp4")

print(capt.getVideoLength())
