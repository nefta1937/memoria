import time 
import random
from datetime import datetime

class Camera:
    _blue_position = None
    _red_position = None
    _yellow_position = None
    _child_blue_position = None
    _child_red_position = None
    _child_yellow_position = None
    _has_to_stop = False

    def __init__(self, blue_position, red_position, yellow_position, child_blue_position, child_red_position, child_yellow_position):
        self._blue_position = blue_position
        self._red_position = red_position
        self._yellow_position = yellow_position
        self._child_blue_position = child_blue_position
        self._child_red_position = child_red_position
        self._child_yellow_position = child_yellow_position

    def stop(self):
        self._has_to_stop = True

    #TODO: Aqui reemplazar la función con líneas funcionales que permiten realizar la lectura
    def start_execution(self):
        while True and self._has_to_stop == False:
            self._blue_position.change_position(random.randint(0, 100), random.randint(0, 100))
            self._red_position.change_position(random.randint(0, 100), random.randint(0, 100))
            self._yellow_position.change_position(random.randint(0, 100), random.randint(0, 100))
            self._child_blue_position.change_position(random.randint(0, 100), random.randint(0, 100))
            self._child_red_position.change_position(random.randint(0, 100), random.randint(0, 100))
            self._child_yellow_position.change_position(random.randint(0, 100), random.randint(0, 100))
            print(datetime.now().strftime('%H:%M:%S') + ': running execution')
            time.sleep(0.5)

