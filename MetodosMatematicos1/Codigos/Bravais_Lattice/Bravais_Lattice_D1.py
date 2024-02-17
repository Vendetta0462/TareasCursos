# Importing the required modules for 3d plotting
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Create 3 base vectors
# Simple Cubic
a1 = np.array([1, 0, 0])
a2 = np.array([0, 1, 0])
a3 = np.array([0, 0, 1])

# Find the reciprocal lattice vectors
a1r = np.cross(a2, a3)/np.dot(a1, np.cross(a2, a3))
a2r = np.cross(a3, a1)/np.dot(a1, np.cross(a2, a3))
a3r = np.cross(a1, a2)/np.dot(a1, np.cross(a2, a3))

#Create a list of n possible vectors
n = 1
vectors = [np.array(i*a1r+j*a2r+k*a3r) for i in range(n+1) for j in range(n+1) for k in range(n+1)]
# vectors = [(0,0,0), a1, a2, a3, a1+a2, a1+a3, a2+a3, 2*a1, 2*a2, 2*a3, a1+a2-a3, a1-a2+a3, -a1+a2+a3, a1+a2+a3]

# vectors = vectors + [a1+a3-a2+v for v in vectors] + [-a1+a3+a2+v for v in vectors] + [2*a3+v for v in vectors]
# vectors = vectors + [a1+a2-a3+v for v in vectors]

#Plot the array of vectors
fig = plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')
ax.set_box_aspect([1,1,1])
ax.scatter3D([v[0] for v in vectors],[v[1] for v in vectors],[v[2] for v in vectors], s=50, color="k")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_xlim(-0.2,1.2)
ax.set_ylim(-0.2,1.2)
ax.set_zlim(-0.2,1.2)

#Connect cube vertices
ax.plot3D([0,1,1,0,0],[0,0,1,1,0],[0,0,0,0,0],color='k',linewidth=3)
ax.plot3D([0,1,1,0,0],[0,0,1,1,0],[1,1,1,1,1],color='k',linewidth=3)
ax.plot3D([0,0],[0,0],[0,1],color='k',linewidth=3)
ax.plot3D([1,1],[0,0],[0,1],color='k',linewidth=3)
ax.plot3D([0,0],[1,1],[0,1],color='k',linewidth=3)
ax.plot3D([1,1],[1,1],[0,1],color='k',linewidth=3)

#Plot the reciprocal primitive vectors
ax.plot([0, a1r[0]], [0, a1r[1]], [0, a1r[2]], color="g", linewidth=3)
ax.plot([0, a2r[0]], [0, a2r[1]], [0, a2r[2]], color="g", linewidth=3)
ax.plot([0, a3r[0]], [0, a3r[1]], [0, a3r[2]], color="g", linewidth=3)

#Show the primitive vector labels
ax.text(a1r[0], a1r[1], a1r[2], "a'", color='g', fontsize=20)
ax.text(a2r[0], a2r[1], a2r[2], "b'", color='g', fontsize=20)
ax.text(a3r[0], a3r[1], a3r[2], "c'", color='g', fontsize=20)



plt.show()