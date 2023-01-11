#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

d=np.loadtxt('neuronasplot.txt')
fig, ax = plt.subplots()
ax.set_title('tasa de error segun el numero de neuronas');
ax.grid();
ax.set_xlim([10,2100]);
ax.set_xlabel('Epoch');
ax.set_ylim([7,14]);
ax.set_ylabel('error de clasificación');
ax.plot(d[:,0], d[:,1], label='g=1', lw=2, marker='o', markersize=5, color='blue')
ax.legend()
plt.savefig('neuronasplot.pdf');
plt.show();
