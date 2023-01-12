#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

d=np.loadtxt('epochplot.txt')
fig, ax = plt.subplots()
ax.set_title('tasa de error segun el numero de epocas');
ax.grid();
ax.set_xlim([0,31]);
ax.set_xlabel('Epoch');
ax.set_ylim([7,20]);
ax.set_ylabel('error de clasificación');
ax.plot(d[:,0], d[:,1], lw=2, marker='o', markersize=5, color='blue')
ax.legend()
plt.savefig('epochplot.pdf');
plt.show();
