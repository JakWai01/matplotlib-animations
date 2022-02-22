import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

g = 9.81 

x0, y0 = 0, 5 

vx0, vy0 = 1, 0

dt = 0.005

XMAX = 5

# A restitution of 1 means that no energy is lost in a collision
RESTITUTION = 0.65 

def get_pos():
    x, y, vy = 0, y0, vy0
    while x < XMAX:
        y += vy * dt
        x += vx0 * dt
        vy -= g * dt
        if y < 0:
            y = 0 
            vy = -vy * RESTITUTION 
        yield x, y, vy

def init():
    ax[0].set_ylim(0, y0)
    ax[0].set_xlim(0, XMAX)
    ax[0].set_ylabel('height in m')
    ax[0].set_xlabel('distance in m')
    ax[1].set_ylim(-10, 10)
    ax[1].set_xlim(0, XMAX)
    ax[1].set_ylabel('v in m/s')
    ax[1].set_xlabel('time in s')
    ax[2].set_ylim(0, y0)
    ax[2].set_xlim(0, XMAX)
    ax[2].set_ylabel('height in m')
    ax[2].set_xlabel('distance in m')
    ball.set_center((x0, y0))
    line.set_data(xdata, vdata)
    path.set_data(xdata, ydata)
    return ball, line, path


def update(pos):
    x, y, vy = pos 
    xdata.append(x)
    ydata.append(y)
    vdata.append(vy)
    ball.set_center((x, y))
    line.set_data(xdata, vdata)
    path.set_data(xdata, ydata)
    return ball, line, path

fig, ax = plt.subplots(3)
ax[0].set_aspect('equal')

xdata, ydata, vdata = [], [], []

ball = plt.Circle((x0, y0), 0.08)
line, = ax[1].plot([], [], lw=2)
path, = ax[2].plot([], [], lw=2)

ax[0].add_patch(ball)

animation = FuncAnimation(fig, update, get_pos, blit=True, interval=1000*dt,
        repeat=False, init_func=init)

plt.show()
