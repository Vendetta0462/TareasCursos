#import common libraries for 3d plotting
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#Create 3 base vectors 
a1 = np.array([1,0,0])
a2 = np.array([0,1,0])
a3 = np.array([1/2,1/2,1/2])

#Create a list of n possible vectors
n = 2
# vectors = [np.array(i*a1+j*a2+k*a3) for i in range(-1,n+1) for j in range(-1,n+1) for k in range(-1,n+1)]
vectors = [(0,0,0), a1, a2, a3, a1+a2, -a1-a2+2*a3, 2*a3, 2*a3-a1, 2*a3-a2]

#append the double of vectors to the list
# vectors = vectors + [a1+v for v in vectors] + [a2+v for v in vectors] + [a1+a2+v for v in vectors]
# vectors = vectors + [2*a3-a1-a2+v for v in vectors]

#Plot the array of vectors
fig = plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')
ax.set_box_aspect([1,1,1])
ax.scatter3D([v[0] for v in vectors],[v[1] for v in vectors],[v[2] for v in vectors], s=50, color="k")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_xlim3d(-0.2, 1.2)
ax.set_ylim3d(-0.2, 1.2)
ax.set_zlim3d(-0.2, 1.2)
# ax.set_xlim3d(-n, n)
# ax.set_ylim3d(-n, n)
# ax.set_zlim3d(-n, n)

#Connect cube vertices
# ax.plot3D([0,1,1,0,0],[0,0,1,1,0],[0,0,0,0,0],color='k',linewidth=3)
# ax.plot3D([0,1,1,0,0],[0,0,1,1,0],[1,1,1,1,1],color='k',linewidth=3)
# ax.plot3D([0,0],[0,0],[0,1],color='k',linewidth=3)
# ax.plot3D([1,1],[0,0],[0,1],color='k',linewidth=3)
# ax.plot3D([0,0],[1,1],[0,1],color='k',linewidth=3)
# ax.plot3D([1,1],[1,1],[0,1],color='k',linewidth=3)

#Function that connects the vertices of a cube with a given starting point
def connect_cube(start):
    ax.plot3D([start[0],start[0]+1],[start[1],start[1]],[start[2],start[2]],color='k',linewidth=3)
    ax.plot3D([start[0],start[0]+1],[start[1],start[1]],[start[2]+1,start[2]+1],color='k',linewidth=3)
    ax.plot3D([start[0],start[0]],[start[1],start[1]],[start[2],start[2]+1],color='k',linewidth=3)
    ax.plot3D([start[0]+1,start[0]+1],[start[1],start[1]],[start[2],start[2]+1],color='k',linewidth=3)
    ax.plot3D([start[0],start[0]],[start[1]+1,start[1]+1],[start[2],start[2]+1],color='k',linewidth=3)
    ax.plot3D([start[0]+1,start[0]+1],[start[1]+1,start[1]+1],[start[2],start[2]+1],color='k',linewidth=3)
    ax.plot3D([start[0],start[0]+1],[start[1]+1,start[1]+1],[start[2],start[2]],color='k',linewidth=3)
    ax.plot3D([start[0],start[0]+1],[start[1]+1,start[1]+1],[start[2]+1,start[2]+1],color='k',linewidth=3)
    ax.plot3D([start[0],start[0]],[start[1],start[1]+1],[start[2],start[2]],color='k',linewidth=3)
    ax.plot3D([start[0]+1,start[0]+1],[start[1],start[1]+1],[start[2],start[2]],color='k',linewidth=3)
    ax.plot3D([start[0],start[0]],[start[1],start[1]+1],[start[2]+1,start[2]+1],color='k',linewidth=3)
    ax.plot3D([start[0]+1,start[0]+1],[start[1],start[1]+1],[start[2]+1,start[2]+1],color='k',linewidth=3)

#Connect the cubes
connect_cube((0,0,0))
# connect_cube((1,0,0))
# connect_cube((0,1,0))
# connect_cube((1,1,0))
# connect_cube((0,0,1))
# connect_cube((1,0,1))
# connect_cube((0,1,1))
# connect_cube((1,1,1))

#Create a function that plots primitive vectors depending on start point
def plot_vectors(start):
    ax.plot3D([start[0],start[0]+a1[0]],[start[1],start[1]+a1[1]],[start[2],start[2]+a1[2]],color='g',linewidth=3)
    ax.plot3D([start[0],start[0]+a2[0]],[start[1],start[1]+a2[1]],[start[2],start[2]+a2[2]],color='g',linewidth=3)
    ax.plot3D([start[0],start[0]+a3[0]],[start[1],start[1]+a3[1]],[start[2],start[2]+a3[2]],color='g',linewidth=3)

#Plot the primitive vectors
plot_vectors((0,0,0))
# plot_vectors((1,0,0))
# plot_vectors((0,1,0))
# plot_vectors((1,1,0))
# plot_vectors((0,0,1))
# plot_vectors((1,0,1))
# plot_vectors((0,1,1))
# plot_vectors((1,1,1))
#Plot primitive vectors
# ax.plot([0,a1[0]],[0,a1[1]],[0,a1[2]],color='g', linewidth=3)
# ax.plot([0,a2[0]],[0,a2[1]],[0,a2[2]],color='g', linewidth=3)
# ax.plot([0,a3[0]],[0,a3[1]],[0,a3[2]],color='g', linewidth=3)

#Show primitive vectors labels
ax.text(a1[0],a1[1],a1[2],'a',color='g', fontsize=20)
ax.text(a2[0],a2[1],a2[2],'b',color='g', fontsize=20)
ax.text(a3[0],a3[1],a3[2],'c',color='g', fontsize=20)


plt.show()

