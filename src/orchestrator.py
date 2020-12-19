import threading
from position import Position
from camera import Camera

class Orchestrator:

    _blue_position = None
    _red_position = None
    _yellow_position = None
    _child_blue_position = None
    _child_red_position = None
    _child_yellow_position = None
    _camera = None

    def __init__(self):
        self._blue_position = Position()
        self._red_position = Position()
        self._yellow_position = Position()
        self._child_blue_position = Position()
        self._child_red_position = Position()
        self._child_yellow_position = Position()

    def _run_camera_async(self):
        self._camera = Camera(
            self._blue_position,
            self._red_position,
            self._yellow_position,
            self._child_blue_position,
            self._child_red_position,
            self._child_yellow_position
        )
        thread = threading.Thread(target=self._camera.start_execution)
        thread.start()
        return thread

    def run(self):
        thread_camera = self._run_camera_async()
        print('process initiated')

    def stop(self):
        self._camera.stop()

