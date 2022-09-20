import matplotlib.pyplot as plt
import numpy as np
    
sigma = 1

x = np.linspace(0, 5, 100)
y = 1-np.exp(-sigma*x)
z = (x)**-0.5
w = (1-np.exp(-sigma*x))/x**0.5

plt.figure()
plt.plot(x, y)
plt.plot(x, z)

plt.xlabel('$CL$')
plt.ylabel('Signal and Noise')

#plt.yticks([])
plt.xticks(np.arange(6), ('0', '$1/\sigma$','$2/\sigma$','$3/\sigma$','$4/\sigma$','$5/\sigma$'))
#plt.yticks(np.arange(3), ('0', '$\lambda/2$','$\lambda$'))

#plt.text(-0.2,0,'0',fontsize=12,color='k')
#plt.text(-0.2,1, '$\\lambda$',fontsize=12,color='k')

plt.savefig('optimumlengthone.png', edgecolor='w', bbox_inches='tight')
plt.show()


plt.figure()
plt.plot(x, w)

plt.xlabel('$CL$')
plt.ylabel('Signal to Noise Ratio')

#plt.yticks([])
plt.xticks(np.arange(6), ('0', '$1/\sigma$','$2/\sigma$','$3/\sigma$','$4/\sigma$','$5/\sigma$'))
#plt.yticks(np.arange(3), ('0', '$\lambda/2$','$\lambda$'))

#plt.text(-0.2,0,'0',fontsize=12,color='k')
#plt.text(-0.2,1, '$\\lambda$',fontsize=12,color='k')

plt.savefig('optimumlengthtwo.png', edgecolor='w', bbox_inches='tight')
plt.show()

