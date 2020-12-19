import threading
import time
from camera import Camera
from position import Position

def test():
    blue_position = Position()
    red_position = Position()
    yellow_position = Position()
    child_blue_position = Position()
    child_red_position = Position()
    child_yellow_position = Position()

    camera = Camera(blue_position, red_position, yellow_position, child_blue_position, child_red_position, child_yellow_position)
    thread = threading.Thread(target=camera.start_execution)
    thread.start()

    index = 0
    blue_position_list = []
    red_position_list = []
    yellow_position_list = []
    child_blue_position_list = []
    child_red_position_list = []
    child_yellow_position_list = []
    while(index < 10):
        blue_position_list.append(str(blue_position.x) + "," + str(blue_position.y))
        red_position_list.append(str(red_position.x) + "," + str(red_position.y))
        yellow_position_list.append(str(yellow_position.x) + "," + str(yellow_position.y))
        child_blue_position_list.append(str(child_blue_position.x) + "," + str(child_blue_position.y))
        child_red_position_list.append(str(child_red_position.x) + "," + str(child_red_position.y))
        child_yellow_position_list.append(str(child_yellow_position.x) + "," + str(child_yellow_position.y))

        time.sleep(0.49)
        index = index + 1
    
    camera.stop()
    thread.join()

    print(len(list(set(blue_position_list))))
    print(list(set(blue_position_list)))

    if(len(list(set(blue_position_list))) < 7):
        raise Exception("camera test was not success")
    if(len(list(set(red_position_list))) < 2):
        raise Exception("camera test was not success")
    if(len(list(set(yellow_position_list))) < 2):
        raise Exception("camera test was not success")
    if(len(list(set(child_blue_position_list))) < 2):
        raise Exception("camera test was not success")
    if(len(list(set(child_red_position_list))) < 2):
        raise Exception("camera test was not success")
    if(len(list(set(child_yellow_position_list))) < 2):
        raise Exception("camera test was not success")

test()
