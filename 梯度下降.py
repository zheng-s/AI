
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-1,6,141)
y=(x-2.5)**2-1
plt.plot(x,y)
plt.show()
def dj(theta):
    return 2*(theta-2.5)
#求导函数
def j(theta):
    try:
        return(theta-2.5)**2-1
    except:
        return float('inf')
#损失函数
def gd(initial_theta,eta,n_iters=1e4,error=1e-8):#10的四次方,10的-8次方
    theta=initial_theta
    theta_history.append(initial_theta)
    i_iters=0
    
    while i_iters<n_iters:
        g=dj(theta)
        last_theta=theta
        theta=theta-g*eta
        theta_history.append(theta)
        if(abs(j(theta)-j(last_theta))<error):#还可以换成abs(j)小于error
            break
        i_iters+=1
def plot_thetahistory():
    plt.plot(x,j(x))
    plt.plot(theta_history,j(np.array(theta_history)),color='r',marker='+')
    plt.show()
    
eta=0.01
theta_history=[]
gd(0,eta)
plot_thetahistory()
        
        
        