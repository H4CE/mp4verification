import pytest
from datetime import time
from proxima.transcoded_file import TranscodedFile, assertThat

# Run all test cases like -
# python -O -m pytest --html=report.html --self-contained-html 
# -q test_layout_switching.py --path "path\to\mp4\file"


def test_layout_detection(path):
    transcodedFile = TranscodedFile(path)
    assert transcodedFile.hasVbssLayoutAt(time(0,0,18))\
                         .hasVbssLayoutAt(time(0,0,30))


#def test_static_image(path):
#    transcodedFile = TranscodedFile(path)
#    assert transcodedFile.getVideoFrameAt(time(0,0,25))\
#                         .onPane(1)\
#                         .hasText("C")


def test_metadata(path):
    transcodedFile = TranscodedFile(path)
    assert transcodedFile.hasVideoFrames(254)\
                         .hasAudioFrames(499)\
                         .hasPlaybackLength(time(0,0,33))

