import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 30, 100)
y = 1*np.exp(-x*x/0.02)

plt.figure()
plt.plot(x, y)
plt.xlabel('$t$')
plt.ylabel('$stimulus$')


plt.yticks([])
#plt.axis('off')
plt.savefig('gaussian.png', edgecolor='w', bbox_inches='tight')

plt.show()
