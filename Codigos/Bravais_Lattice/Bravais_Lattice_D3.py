# Importing the required modules for 3d plotting
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Create 3 base vectors 
# Body Centered Cubic
c1 = np.array([-1, 1, 1])/2
c2 = np.array([1, -1, 1])/2
c3 = np.array([1, 1, -1])/2

# Find the reciprocal lattice vectors
c1r = np.cross(c2, c3)/np.dot(c1, np.cross(c2, c3))
c2r = np.cross(c3, c1)/np.dot(c1, np.cross(c2, c3))
c3r = np.cross(c1, c2)/np.dot(c1, np.cross(c2, c3))

#Create a list of n possible vectors
n = 1
# vectors = [np.array(i*c1r+j*c2r+k*c3r) for i in range(-n, n+1) for j in range(-n, n+1) for k in range(-n, n+1)]
vectors = [(0,0,0), c1r, c2r, c3r, c1r+c2r, c1r+c3r, c2r+c3r, c1r+c2r+c3r]
# vectors = [(0,0,0), -(c1r+c2r+c3r), c1r, c2r, c3r, -c1r, -c2r, -c3r, c1r+c2r+c3r]

# vectors = vectors + [c1+c3-c2+v for v in vectors] + [-c1+c3+c2+v for v in vectors] + [2*c3+v for v in vectors]
# vectors = vectors + [c1+c2-c3+v for v in vectors]

#Plot the array of vectors
fig = plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')
ax.set_box_aspect([1,1,1])
ax.scatter3D([v[0] for v in vectors],[v[1] for v in vectors],[v[2] for v in vectors], s=50, color="k")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_xlim(-0.7,2.2)
ax.set_ylim(-0.7,2.2)
ax.set_zlim(-0.7,2.2)
# ax.set_zlim(-n-1,n+1)
# ax.set_ylim(-n-1,n+1)
# ax.set_xlim(-n-1,n+1)

#Create the unit cell
ax.plot([c3r[0], c3r[0]+c2r[0], c3r[0]+c2r[0]+c1r[0], c3r[0]+c1r[0], c3r[0]],
        [c3r[1], c3r[1]+c2r[1], c3r[1]+c2r[1]+c1r[1], c3r[1]+c1r[1], c3r[1]],
        [c3r[2], c3r[2]+c2r[2], c3r[2]+c2r[2]+c1r[2], c3r[2]+c1r[2], c3r[2]], color="k", linewidth=3)
ax.plot([c1r[0], c1r[0]+c2r[0], c2r[0]], [c1r[1], c1r[1]+c2r[1], c2r[1]],
        [c1r[2], c1r[2]+c2r[2], c2r[2]], color="k", linewidth=3)
ax.plot([c1r[0], c1r[0]+c3r[0], c1r[0]+c3r[0]+c2r[0], c1r[0]+c2r[0], c2r[0], c2r[0]+c3r[0]],
        [c1r[1], c1r[1]+c3r[1], c1r[1]+c3r[1]+c2r[1], c1r[1]+c2r[1], c2r[1], c2r[1]+c3r[1]],
        [c1r[2], c1r[2]+c3r[2], c1r[2]+c3r[2]+c2r[2], c1r[2]+c2r[2], c2r[2], c2r[2]+c3r[2]], color="k", linewidth=3)

#Plot original vectors
ax.plot([0,c1[0]],[0,c1[1]],[0,c1[2]], color="r", linewidth=3)
ax.plot([0,c2[0]],[0,c2[1]],[0,c2[2]], color="r", linewidth=3)
ax.plot([0,c3[0]],[0,c3[1]],[0,c3[2]], color="r", linewidth=3)

#Plot the reciprocal primitive vectors
ax.plot([0, c1r[0]], [0, c1r[1]], [0, c1r[2]], color="g", linewidth=3)
ax.plot([0, c2r[0]], [0, c2r[1]], [0, c2r[2]], color="g", linewidth=3)
ax.plot([0, c3r[0]], [0, c3r[1]], [0, c3r[2]], color="g", linewidth=3)

#Show the original vector labels
ax.text(c1[0], c1[1], c1[2], "a", color="r", fontsize=20)
ax.text(c2[0], c2[1], c2[2], "b", color="r", fontsize=20)
ax.text(c3[0], c3[1], c3[2], "c", color="r", fontsize=20)

#Show the primitive vector labels
ax.text(c1r[0], c1r[1], c1r[2], "a'", color='g', fontsize=20)
ax.text(c2r[0], c2r[1], c2r[2], "b'", color='g', fontsize=20)
ax.text(c3r[0], c3r[1], c3r[2], "c'", color='g', fontsize=20)


plt.show()
