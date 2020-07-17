import pickle
import matplotlib.pyplot as plt

f = open('output.pckl', 'rb')
eps, ez = pickle.load(f)
f.close()

plt.figure()
plt.imshow(eps.transpose(), interpolation='spline36', cmap='binary')
plt.axis('off')
plt.savefig('eps.png')

plt.figure()
plt.imshow(eps.transpose(), interpolation='spline36', cmap='binary')
plt.imshow(ez.transpose(), interpolation='spline36', cmap='RdBu', alpha=0.9)
plt.axis('off')
plt.savefig('ez.png')