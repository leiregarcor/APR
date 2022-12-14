#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

d=np.loadtxt('linear.out')
fig, ax = plt.subplots()
ax.set_title('kernel lineal en MNIST con tr 12k y dv 6k');
ax.grid();
ax.set_xscale('log');
ax.set_xlim([1.5e-1,1.5e1]);
ax.set_xlabel('C');
ax.set_ylim([8,15]);
ax.set_ylabel('error de clasificación');
ax.plot(d[:,0], d[:,1], label='tr', lw=2, marker='o', markersize=10)
ax.plot(d[:,0], d[:,2], label='dv', lw=2, marker='x', markersize=10)
ax.legend();
plt.savefig('linear.pdf');
plt.show();
