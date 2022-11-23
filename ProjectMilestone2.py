import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft
t= np.linspace(0,3,12*1024)
Fi=[392,0,261.63,261.63,261.63,0,293.66,329.63,329.63]
fi=[0,0,0,0,0,0,0,0,0]
ti=[0,0.5,0.9,1.2,1.4,1.6,2,2.3,3]
Ti=[0.5,0.4,0.3,0.2,0.2,0.4,0.3,0.2,0.5]
i=0
def u(t):
    return 1*(t>0)
s=np.multiply((np.sin(2*(np.pi)*0*t)+(np.sin(2*(np.pi)*0*t))),((u(t-ti[i]))-(u((t-t[i]-Ti[i])))))
for i in range (0,len(Fi)):
    x= np.multiply((np.sin(2*(np.pi)*Fi[i]*t)+(np.sin(2*(np.pi)*fi[i]*t))),((u(t-ti[i]))-(u((t-ti[i]-Ti[i])))))    
    s= s+x
plt.subplot(3,2,1) #the original song
plt.plot(t,s)
N= 3*1024
f= np.linspace(0,512,int(N/2))
sf= fft(s)
sf= 2/N*np.abs(sf[0:np.int(N/2)])
plt.subplot(3,2,2) #the transformed original song
plt.plot(f,sf)
fn1= np.random.randint(0,512,1)
fn2= np.random.randint(0,512,1) 
n= (np.sin(2*fn1*(np.pi)*t))+(np.sin(2*fn2*(np.pi)*t))
xn= s+n
plt.subplot(3,2,3) #the noisy song
plt.plot(t,xn)
xnf= fft(xn)
xnf= 2/N*np.abs(xnf[0:np.int(N/2)])
plt.subplot(3,2,4) #the transformed noisy song
plt.plot(f,xnf)
max= round(max(sf))
ind1= []
while(i<len(xnf)):
    if(round(xnf[i])>max):
        ind1.append(i)
    i+=1
fn11= round(f[ind1[0]]) 
fn22= round(f[ind1[1]])  
xfilter= xn - ((np.sin(2*fn11*(np.pi)*t))+(np.sin(2*fn22*(np.pi)*t)))
plt.subplot(3,2,5) #the filtered song
plt.plot(t,xfilter)
xfilterf= fft(xfilter)
xfilterf= 2/N*np.abs(xfilterf[0:np.int(N/2)])
plt.subplot(3,2,6) #the transformed filter song
plt.plot(f,xfilterf)
sd.play(xfilter, 3*1024)