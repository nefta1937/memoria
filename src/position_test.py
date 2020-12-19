from position import Position

def run_test():
    pos1 = Position()
    pos1.change_position(10, 20)
    
    if(pos1.x != 10):
        raise Exception("Position test not was success")
    if(pos1.y != 20):
        raise Exception("Position test not was success")


run_test()