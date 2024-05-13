import numpy as np
import matplotlib.pyplot as plt

a = 100
l = 50
t = 4 
n = 50
d_x = l/n
d_y = l/n
d_t = min(d_x**2/(4*a), d_y**2/(4*a))

t_n = int(t/d_t)

u = np.zeros((n,n)) + 25


#u[:,-1] = 100
#u[:,0] = 100
u[0,:] = 100
u[-1,:] = 100



fig, axis = plt.subplots()
pcm = axis.pcolormesh(u, cmap=plt.cm.jet, vmin=0, vmax=100)

teller = 0

while teller < t:
    w = u.copy()

    for i in range(1, n -1):
        for j in range(1,n-1):

            dd_ux = (w[i-1,j]- 2*w[i,j] + w[i+1, j])/(d_x**2)
            dd_uy = (w[i,j-1]- 2*w[i,j] + w[i, j+1])/(d_y**2)

            u[i,j] = d_t*a*(dd_ux + dd_uy) + w[i,j]
    
    teller += d_t

    pcm.set_array(u)
    plt.pause(0.001)

plt.show()