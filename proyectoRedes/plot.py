#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

d=np.loadtxt('lrplot.txt')
fig, ax = plt.subplots()
ax.set_title('tasa de error segun el learning-rate');
ax.grid();
ax.set_xscale('log');
ax.set_xlim([1.5e-6,1]);
ax.set_xlabel('Learning-rate');
ax.set_ylim([7,75]);
ax.set_ylabel('error de clasificación');
ax.plot(d[:,0], d[:,1], lw=2, marker='o', markersize=5, color='blue')
ax.legend()
plt.savefig('lrplot.pdf');
plt.show();
