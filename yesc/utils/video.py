import cv2
from contextlib import contextmanager


@contextmanager
def open_video(*args):
    '''
    OpenCV2 video capture wrapper. 
    @author Jordi Yaputra.
    
    This returns a frame generator that can be iterated to produce
    video frames

    Usage example:
    ```
        with open_video(0) as video:
            for frame in video:
                # Do something with the video frame
                # Press `q` to stop the video.
    ```
    '''
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
