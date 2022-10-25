import matplotlib.pyplot as plt
# set up the figure
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(0,10)
ax.set_ylim(0,10)

# draw lines
xmin = 1
xmax = 9
y = 5
height = 1

plt.hlines(y, xmin, xmax+2)
plt.vlines([1,2,3,4,5,6,7,8,9], y - height / 2., y + height / 2.)
plt.vlines(xmax, y - height / 2., y + height / 2.)

# draw a point on the line
px = 8.5
plt.plot(px,y, 'ro', ms = 15, mfc = 'r')


plt.text(5,y-2,'length',horizontalalignment='center')

# add numbers
plt.text(xmin, y-1, '0', horizontalalignment='center')
plt.text(xmax, y-1, '$x+dx$', horizontalalignment='center')
plt.text(xmax-1, y-1, 'x', horizontalalignment='center')


plt.axis('off')
plt.savefig('bergplot.png', edgecolor='w', bbox_inches='tight')
plt.show()

