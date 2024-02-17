# Importing the required modules for 3d plotting
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Create 3 base vectors 
# Body Centered Cubic
b1 = np.array([1, 0, 0])
b2 = np.array([0, 1, 0])
b3 = np.array([1, 1, 1])/2

# Find the reciprocal lattice vectors
b1r = np.cross(b2, b3)/np.dot(b1, np.cross(b2, b3))
b2r = np.cross(b3, b1)/np.dot(b1, np.cross(b2, b3))
b3r = np.cross(b1, b2)/np.dot(b1, np.cross(b2, b3))

#Create a list of n possible vectors
n = 1
# vectors = [np.array(i*b1r+j*b2r+k*b3r) for i in range(-n, n+1) for j in range(-n, n+1) for k in range(-n, n+1)]
vectors = [(0,0,0), b1r, b2r, b3r, b1r+b2r, b1r+b3r, b2r+b3r, b1r+b2r+b3r]

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
ax.set_zlim(-2.2,1.2)
# ax.set_zlim(-n-1,n+1)
# ax.set_ylim(-n-1,n+1)
# ax.set_xlim(-n-1,n+1)

#Create the unit cell
ax.plot([b3r[0], b3r[0]+b2r[0], b3r[0]+b2r[0]+b1r[0], b3r[0]+b1r[0], b3r[0]],
        [b3r[1], b3r[1]+b2r[1], b3r[1]+b2r[1]+b1r[1], b3r[1]+b1r[1], b3r[1]],
        [b3r[2], b3r[2]+b2r[2], b3r[2]+b2r[2]+b1r[2], b3r[2]+b1r[2], b3r[2]], color="k", linewidth=3)
ax.plot([b1r[0], b1r[0]+b2r[0], b2r[0]], [b1r[1], b1r[1]+b2r[1], b2r[1]],
        [b1r[2], b1r[2]+b2r[2], b2r[2]], color="k", linewidth=3)
ax.plot([b1r[0], b1r[0]+b3r[0], b1r[0]+b3r[0]+b2r[0], b1r[0]+b2r[0], b2r[0], b2r[0]+b3r[0]],
        [b1r[1], b1r[1]+b3r[1], b1r[1]+b3r[1]+b2r[1], b1r[1]+b2r[1], b2r[1], b2r[1]+b3r[1]],
        [b1r[2], b1r[2]+b3r[2], b1r[2]+b3r[2]+b2r[2], b1r[2]+b2r[2], b2r[2], b2r[2]+b3r[2]], color="k", linewidth=3)

#Plot original vectors
ax.plot([0,b1[0]],[0,b1[1]],[0,b1[2]], color="r", linewidth=3)
ax.plot([0,b2[0]],[0,b2[1]],[0,b2[2]], color="r", linewidth=3)
ax.plot([0,b3[0]],[0,b3[1]],[0,b3[2]], color="r", linewidth=3)

#Plot the reciprocal primitive vectors
ax.plot([0, b1r[0]], [0, b1r[1]], [0, b1r[2]], color="g", linewidth=3)
ax.plot([0, b2r[0]], [0, b2r[1]], [0, b2r[2]], color="g", linewidth=3)
ax.plot([0, b3r[0]], [0, b3r[1]], [0, b3r[2]], color="g", linewidth=3)

#Show the original vector labels
ax.text(b1[0], b1[1], b1[2], "a", color="r", fontsize=20)
ax.text(b2[0], b2[1], b2[2], "b", color="r", fontsize=20)
ax.text(b3[0], b3[1], b3[2], "c", color="r", fontsize=20)

#Show the primitive vector labels
ax.text(b1r[0], b1r[1], b1r[2], "a'", color='g', fontsize=20)
ax.text(b2r[0], b2r[1], b2r[2], "b'", color='g', fontsize=20)
ax.text(b3r[0], b3r[1], b3r[2], "c'", color='g', fontsize=20)


plt.show()
