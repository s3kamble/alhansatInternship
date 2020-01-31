import matplotlib.pyplot as plt 
from matplotlib import animation
import numpy as np

def f(x):
      y1= np.sin(x)
      y2=x**2/4
      y=y1-y2
      return y

def limit():
     for i in range (10):
         ans= f(i)
         if ans<0:
               return i

maxm=limit()
minm=maxm-1

l1=[]
l2=[]
def graphical(minm,maxm):
      global l1,l2
      a=np.arange(minm,maxm+0.0001,0.1)
      for i in range(0,a.size):
                   ans=f(a[i])
                   l1.append(ans)
                   l2.append(a[i])
                   if ans<0:
                         a=np.arange(a[i-1],a[i],0.01)
                         for i in range(1,a.size):
                                 
                                 ans=f(a[i])
                                 l1.append(ans)
                                 l2.append(a[i])
                                 if ans<0:
                                       l1.pop(-1)
                                       l2.pop(-1)
                                             
                                       
                                       
    

graphical(minm,maxm)
#print(l1)
#print(l2)


yrange = f(minm), f(maxm)
ymin, ymax = min(yrange), max(yrange) 
vf = np.vectorize(f)
x = np.linspace(minm,maxm)
y = vf(x)
epsilon = 0.1

fig = plt.figure()
ax = plt.axes(xlim=(minm-epsilon,maxm+epsilon), ylim=(ymin,ymax))
curve, = ax.plot([],[], color='blue')
left, = ax.plot([],[],color='red')
right, = ax.plot([],[],color='red')
plt.title("Graphical  method")

# Figure reset between frames
def init():
    left.set_data([],[])
    right.set_data([],[])
    curve.set_data([],[])
    return left, right, curve,

def animate(i):
      
            a, b = l1,l2
            print(a,b)
            c=a.pop(0)
            d=b.pop(0)
            left.set_data([c,c],[ymin,ymax])
            right.set_data([d,d],[ymin,ymax])
            curve.set_data(x,y)
            return left, right, curve,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=15, interval=1000, blit=True)

plt.grid()
plt.show()







      
    







      
    

