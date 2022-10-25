import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3, 100)
y = 1*np.exp(-x)

plt.figure()
plt.plot(x, y)
plt.xlabel('$E/k_BT$')
plt.ylabel('$exp(-E/k_BT)$')

#plt.axis('off')
plt.savefig('exponential.png', edgecolor='w', bbox_inches='tight')

plt.show()
