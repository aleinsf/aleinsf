import matplotlib as mtl
import matplotlib.pyplot as plt

# fig, ax = plt.subplots()
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
# plt.show()

############ pyplot 

plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Simple plot')
plt.show()

############# OOP

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
ax.set_xlabel('x')  
ax.set_ylabel('y')  
ax.set_title('Simple plot OOP')
plt.show()
