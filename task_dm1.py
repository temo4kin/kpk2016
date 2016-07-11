from drawman import *
from time import sleep

drawman_scale(5, 70, 1)
drawman_draw_grid('blue')
axis()
drawman_pen_size(9)
drawman_color("darkblue")

A = [(0, 0), (30, 0), (30, 30), (0, 30)]



pen_down()

for x, y in A:
    to_point(x, y)
to_point(A[0][0], A[0][1])
pen_up()

sleep(3)