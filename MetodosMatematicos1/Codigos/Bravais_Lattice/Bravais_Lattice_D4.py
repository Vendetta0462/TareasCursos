# Importing the required modules for 3d plotting
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Create 3 base vectors 
# Face Centered Cubic
d1 = np.array([0, 1, 1])/2
d2 = np.array([1, 0, 1])/2
d3 = np.array([1, 1, 0])/2

# Find the reciprocal lattice vectors
d1r = np.cross(d2, d3)/np.dot(d1, np.cross(d2, d3))
d2r = np.cross(d3, d1)/np.dot(d1, np.cross(d2, d3))
d3r = np.cross(d1, d2)/np.dot(d1, np.cross(d2, d3))

#Create a list of n possible vectors
n = 1
# vectors = [np.array(i*d1r+j*d2r+k*d3r) for i in range(-n, n+1) for j in range(-n, n+1) for k in range(-n, n+1)]
vectors = [(0,0,0), d1r, d2r, d3r, d1r+d2r, d1r+d3r, d2r+d3r, d1r+d2r+d3r]

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
ax.set_xlim(-1.2,2.2)
ax.set_ylim(-1.2,2.2)
ax.set_zlim(-1.2,2.2)
# ax.set_zlim(-n-1,n+1)
# ax.set_ylim(-n-1,n+1)
# ax.set_xlim(-n-1,n+1)

#Create the unit cell
ax.plot([d3r[0], d3r[0]+d2r[0], d3r[0]+d2r[0]+d1r[0], d3r[0]+d1r[0], d3r[0]],
        [d3r[1], d3r[1]+d2r[1], d3r[1]+d2r[1]+d1r[1], d3r[1]+d1r[1], d3r[1]],
        [d3r[2], d3r[2]+d2r[2], d3r[2]+d2r[2]+d1r[2], d3r[2]+d1r[2], d3r[2]], color="k", linewidth=3)
ax.plot([d1r[0], d1r[0]+d2r[0], d2r[0]], [d1r[1], d1r[1]+d2r[1], d2r[1]],
        [d1r[2], d1r[2]+d2r[2], d2r[2]], color="k", linewidth=3)
ax.plot([d1r[0], d1r[0]+d3r[0], d1r[0]+d3r[0]+d2r[0], d1r[0]+d2r[0], d2r[0], d2r[0]+d3r[0]],
        [d1r[1], d1r[1]+d3r[1], d1r[1]+d3r[1]+d2r[1], d1r[1]+d2r[1], d2r[1], d2r[1]+d3r[1]],
        [d1r[2], d1r[2]+d3r[2], d1r[2]+d3r[2]+d2r[2], d1r[2]+d2r[2], d2r[2], d2r[2]+d3r[2]], color="k", linewidth=3)

#Plot original vectors
ax.plot([0,d1[0]],[0,d1[1]],[0,d1[2]], color="r", linewidth=3)
ax.plot([0,d2[0]],[0,d2[1]],[0,d2[2]], color="r", linewidth=3)
ax.plot([0,d3[0]],[0,d3[1]],[0,d3[2]], color="r", linewidth=3)

#Plot the reciprocal primitive vectors
ax.plot([0, d1r[0]], [0, d1r[1]], [0, d1r[2]], color="g", linewidth=3)
ax.plot([0, d2r[0]], [0, d2r[1]], [0, d2r[2]], color="g", linewidth=3)
ax.plot([0, d3r[0]], [0, d3r[1]], [0, d3r[2]], color="g", linewidth=3)

#Show the original vector labels
ax.text(d1[0], d1[1], d1[2], "a", color="r", fontsize=20)
ax.text(d2[0], d2[1], d2[2], "b", color="r", fontsize=20)
ax.text(d3[0], d3[1], d3[2], "c", color="r", fontsize=20)

#Show the primitive vector labels
ax.text(d1r[0], d1r[1], d1r[2], "a'", color='g', fontsize=20)
ax.text(d2r[0], d2r[1], d2r[2], "b'", color='g', fontsize=20)
ax.text(d3r[0], d3r[1], d3r[2], "c'", color='g', fontsize=20)


plt.show()