import matplotlib.pyplot as plt 
from matplotlib import animation
import numpy as np 

def f(x):
    return x**2-28

def df(x):
    return 2*x

def limit():
     for i in range (1,10):
         ans= f(i)
         if ans>0:
             return i-1
maxm=limit()
l1=[]
l1.append(maxm)

def newtonRaphson(x):
    return x-f(x)/df(x)


def looping():
         global l1
         i=1
         ans1=newtonRaphson(maxm)
         l1.append(ans1)
         i+=1
         while(i>1 and i<6):
            ans1=newtonRaphson(ans1)
            i+=1
            l1.append(ans1)
            
         

looping()

print(l1)
        
xmin,xmax=5,5.4
yrange = f(xmin), f(xmax)
ymin, ymax = min(yrange), max(yrange) 
vf = np.vectorize(f)
x = np.linspace(xmin,xmax)
y = vf(x)
epsilon = 0.1

# Initialize figure
fig = plt.figure()
ax = plt.axes(xlim=(xmin-epsilon,xmax+epsilon), ylim=(ymin,ymax))
curve, = ax.plot([],[], color='blue')
left, = ax.plot([],[],color='red')

right, = ax.plot([],[],color='red')
plt.title("Newton Raphson method")



# Figure reset between frames
def init():
    left.set_data([],[])
    #right.set_data([],[])
    curve.set_data([],[])
    return left, right, curve,

def animate(i):
    a=l1.pop(0)
    
    left.set_data([a,a],[ymin,ymax])
    #right.set_data([b,b],[ymin,ymax])
    curve.set_data(x,y)
    return left, right, curve,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=15, interval=1000, blit=True)

plt.grid()
plt.show()

    













