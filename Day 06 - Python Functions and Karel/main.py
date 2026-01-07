# Goal of this challenge was to create a code which will move robot out of maze. (Reeborg's World, Maze problem)
# Since robot has only command to move forward and turn left, we have to define a command to turn right. 
# That is done by defining a function.

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
# The code works almost all the time, but there are some edge cases where it might get stuck in an infinite loop.
# It is advised by Angela herself to come back to this challenge after day 15 when we have learned about while loops in more detail.