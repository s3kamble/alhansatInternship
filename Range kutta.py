 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

def dydx(x, y): 
	return ((x - y)/2) 
l1=[]
def rungeKutta(x0, y0, x, h):
        global l1
        n = (int)((x - x0)/h)
        y = y0
        for i in range(1, n + 1):
                k1 = h * dydx(x0, y)
                k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1)
                k3 = h * dydx(x0 + 0.5 * h, y + 0.5 * k2)
                k4 = h * dydx(x0 + h, y + k3)
                y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)
                x0 = x0 + h
        l1.append(k1)
        l1.append(k2)
        l1.append(k3)
        l1.append(k4)
        l1.append(y)
        return k1,k2,k3,k4,y

x0 = 0
y = 1
x = 2
h = 0.2
print ('The value of y at x is:', rungeKutta(x0, y, x, h)) 

xmin,xmax=0,1
yrange =0,1
ymin, ymax = min(yrange), max(yrange) 
#vf = np.vectorize(f)
x = np.linspace(xmin,xmax)
#y = vf(x)
epsilon = 0.1

# Initialize figure
fig = plt.figure()
ax = plt.axes(xlim=(xmin-epsilon,xmax+epsilon), ylim=(ymin,ymax))
#curve, = ax.plot([],[], color='blue')
left, = ax.plot([],[],color='red')

right, = ax.plot([],[],color='red')
plt.title("Runge Kutta method")



# Figure reset between frames
def init():
    left.set_data([],[])
    #right.set_data([],[])
    #curve.set_data([],[])
    return left, right, #curve,

def animate(i):
    if (len(l1)>1):
            a=l1.pop(0)
            left.set_data([a,a],[ymin,ymax])
    #right.set_data([b,b],[ymin,ymax])
    #curve.set_data(x,y)
            return left, right, #curve,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=15, interval=1000, blit=True)

plt.grid()
plt.show()
