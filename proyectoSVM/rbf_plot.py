#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

d=np.loadtxt('rbf.out')
fig, ax = plt.subplots()
ax.set_title('kernel rbf en MNIST con tr 12k y dv 6k');
ax.grid();
ax.set_xscale('log');
ax.set_xlim([1.5e-2,1.5e2]);
ax.set_xlabel('C');
ax.set_ylim([-0.5,15]);
ax.set_ylabel('error de clasificación');
ax.plot(d[:,0], d[:,1], label='g=1', lw=2, marker='o', markersize=10, color='blue')
ax.plot(d[:,0], d[:,2], label='g=10', lw=2, marker='o', markersize=10, color='orange')
ax.plot(d[:,0], d[:,3], label='g=20', lw=2, marker='o', markersize=10, color='green')
ax.legend()
plt.savefig('rbfGamma.pdf');
plt.show();
