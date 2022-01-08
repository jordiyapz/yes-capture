import cv2
from contextlib import contextmanager


@contextmanager
def open_video(*args):
    # Code to acquire resource, e.g.:
    video_capture = cv2.VideoCapture(*args)

    def frame_generator():
        while video_capture.isOpened():
            success, frame = video_capture.read()
            if not success:
                break

            yield frame
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        return
    try:
        yield frame_generator()
    finally:
        video_capture.release()
