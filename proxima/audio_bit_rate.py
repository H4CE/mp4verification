from pymediainfo import MediaInfo


class VideoCap:
    path=None
    cap=None
    def __init__(self,path) -> None:
        self.path=path
        self.cap=MediaInfo.parse(path)

    def getAudioBitRate(self):
        for track in self.cap.tracks:
            if track.track_type == "Audio":
                return track.bit_rate
    

capt=VideoCap(r"E:\HMS\Coding\Media\vid1.mp4")

print(capt.getAudioBitRate())
                