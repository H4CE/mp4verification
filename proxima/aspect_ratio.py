import cv2 as cv
import math


class AspectRatio:
    cap = None
    path = None

    def __init__(self, path) -> None:

        self.path = path
        self.cap = cv.VideoCapture(self.path)

    def getVideoWidth(self):
        return int(self.cap.get(cv.CAP_PROP_FRAME_WIDTH))

    def getVideoHeight(self):
        return int(self.cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    def getAspectRatio(self):

        width = self.getVideoWidth()
        height = self.getVideoHeight()

        factor = math.gcd(width, height)
        widthRatio = width // factor
        heightRatio = height // factor

        print(f"Aspect Ratio is {widthRatio}:{heightRatio}")


capt = AspectRatio(f"E:\HMS\Coding\Media\darkvid.mp4")

capt.getAspectRatio()
