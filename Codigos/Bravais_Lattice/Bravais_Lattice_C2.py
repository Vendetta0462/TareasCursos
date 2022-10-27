#import common libraries for 3d plotting
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#Create 3 base vectors 
a1 = np.array([-1,1,1])/2
a2 = np.array([1,-1,1])/2
a3 = np.array([1,1,-1])/2

#Create a list of n possible vectors
n = 2
# vectors = [np.array([i,j,k]) for i in range(-n,n) for j in range(-n,n) for k in range(-n,n)]
vectors = [(0,0,0), -(a1+a2+a3), a1, a2, a3, -a1, -a2, -a3, a1+a2+a3]

vectors = vectors + [a1+a3+v for v in vectors] + [a2+a3+v for v in vectors] + [a1+a2+2*a3+v for v in vectors]
vectors = vectors + [a1+a2+v for v in vectors]

#Plot the array of vectors
fig = plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')
ax.set_box_aspect([1,1,1])
ax.scatter3D([v[0] for v in vectors],[v[1] for v in vectors],[v[2] for v in vectors], s=50, color="k")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_xlim(-0.7,1.7)
ax.set_ylim(-0.7,1.7)
ax.set_zlim(-0.7,1.7)
# ax.set_xlim3d(-n, n)
# ax.set_ylim3d(-n, n)
# ax.set_zlim3d(-n, n)

#Plot primitive vectors
# ax.plot([0,a1[0]],[0,a1[1]],[0,a1[2]],color='g', linewidth=3)
# ax.plot([0,a2[0]],[0,a2[1]],[0,a2[2]],color='g', linewidth=3)
# ax.plot([0,a3[0]],[0,a3[1]],[0,a3[2]],color='g', linewidth=3)

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

#Connect the vertices of the cube
connect_cube(-(a1+a2+a3))
connect_cube(a1)
connect_cube(a2)
connect_cube(a3)
connect_cube(-a1)
connect_cube(-a2)
connect_cube(-a3)
connect_cube(a1+a2+a3)

#Create a function that plots primitive vectors depending on start point
def plot_vectors(start):
    ax.plot3D([start[0],start[0]+a1[0]],[start[1],start[1]+a1[1]],[start[2],start[2]+a1[2]],color='g',linewidth=3)
    ax.plot3D([start[0],start[0]+a2[0]],[start[1],start[1]+a2[1]],[start[2],start[2]+a2[2]],color='g',linewidth=3)
    ax.plot3D([start[0],start[0]+a3[0]],[start[1],start[1]+a3[1]],[start[2],start[2]+a3[2]],color='g',linewidth=3)

#Plot primitive vectors
plot_vectors((0,0,0))
plot_vectors(a1+a2)
plot_vectors(a1+a3)
plot_vectors(a2+a3)
plot_vectors(2*a1+a2+a3)
plot_vectors(a1+2*a2+a3)
plot_vectors(a1+a2+2*a3)
plot_vectors(2*a1+2*a2+2*a3)




#Show primitive vectors labels
ax.text(a1[0],a1[1],a1[2],'a',color='g', fontsize=20)
ax.text(a2[0],a2[1],a2[2],'b',color='g', fontsize=20)
ax.text(a3[0],a3[1],a3[2],'c',color='g', fontsize=20)


plt.show()