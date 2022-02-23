import matplotlib.pyplot as plt
import math
from matplotlib.animation import FuncAnimation

# In this animation, we don't respect physics

XMAX = 10
dt = 0.004

def get_pos():
    x, y = 0, 0 
    index = 0

    while x < XMAX:
        x += dt
        y = math.sqrt((XMAX/2)**2 - (x - (XMAX/2))**2) 
        index += 1

        yield x, y, index

def init():
    ax.set_ylim(0, XMAX) 
    ax.set_xlim(0, XMAX)
    ball.set_center((XMAX/2, 0))
    line.set_data(xdata, ydata)
    ln2.set_data(xdata, ydata)
    ln1.set_data(xdata, ydata)
    
    return ball, line, ln2, ln1

def update(pos):
    x, y, index = pos
    xdata.append(x)
    ydata.append(y)
    
    line.set_data(xdata, ydata)
    ln2.set_data(xdata[-90:-50], ydata[-90:-50])
    ln1.set_data(xdata[-50:], ydata[-50:])

    return line, ln2, ln1

fig, ax = plt.subplots()
ax.set_aspect(1)

xdata, ydata = [], []

ball = plt.Circle((XMAX/2, 0), XMAX/math.pi)

# Trajectory
line, = ax.plot([], [], '--', linewidth = 2, color = 'orange')

# Rocket
ln2, = ax.plot([], [], linewidth = 2, color = 'tomato')
ln1, = ax.plot([], [], linewidth = 5, color = 'lightblue')

ax.add_patch(ball)

animation = FuncAnimation(fig, update, get_pos, blit=True, interval=1000*dt,
        repeat=False, init_func=init)

plt.show()
