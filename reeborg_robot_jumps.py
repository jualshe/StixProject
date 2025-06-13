def turn_right():
    turn_left()
    turn_left()
    turn_left()


def do_jump():
    turn_left()
    while wall_on_right():
        if at_goal() == True:
            done()
        elif wall_in_front():
            turn_left()
        else:
            move()
    turn_right()
    move()
    turn_right()
    move()


while at_goal() != True:
    if wall_in_front():
        do_jump()
    else:
        move()


# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# while front_is_clear():
#     move()
# turn_left()
#
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#     if front_is_clear():
#         move()
#     if wall_in_front() and wall_on_right():
#         turn_left()