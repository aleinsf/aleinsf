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

############# 
import numpy as np

x = np.linspace(0, 2, 100)

plt.figure(figsize=(100,50), layout="constrained")
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')   
plt.title("Simple plot")
plt.legend()
plt.show()

############# OOP

x = np.linspace(0, 2, 100)

fig, ax = plt.subplots()
ax.plot(x, x, label='linear')   
ax.plot(x, x**2, label='quadratic') 
ax.plot(x, x**3, label='cubic') 
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title("Simple plot OOP")
ax.legend()
plt.show()

