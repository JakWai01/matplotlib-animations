import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

"""Notes
fig
    Figure object used to get needed events, such as draw or resize
func
    The function to call each frame. The first argument will be the next value in frames. 
frames 
    The values in frames are passed through to the user-supplied func
blit 
    Whether blitting is used to optimize drawing
interval
    Delay between frames in milliseconds
repeat 
    Whether the animation repeats 
init_func
    A function used to draw a clear frame
"""

g = 9.81 

x0, y0 = 0.5, 5
vy0 = 0

dt = 0.005

def get_pos():
    y, vy = y0, vy0
    while y > 0: 
       y += vy * dt 
       vy -= g * dt
       yield 0.5, y

def init():
    ax.set_ylim(0, y0)
    ax.set_ylabel('height in m')
    ball.set_center((x0, y0))
    return ball

def animate(pos):
    x, y = pos
    xdata.append(x)
    ydata.append(y)
    ball.set_center((x, y))
    return ball

fig, ax = plt.subplots()
ax.set_aspect('equal')

xdata, ydata = [], []

ball = plt.Circle((x0, y0), 0.08)
ax.add_patch(ball)

animation = FuncAnimation(fig, animate, get_pos, blit=True, interval=1000*dt, 
        repeat=False, init_func=init)

plt.show()
