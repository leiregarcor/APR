#!/usr/bin/env python
import sys
import numpy as np
from sklearn import svm

if len(sys.argv)!=5:
  print('Usage: %s <tr.npz> <trl.npz> <dv.npz> <dvl.npz>' % sys.argv[0]);
  sys.exit(1);

tr=np.load(sys.argv[1]);  tr=tr[tr.files[0]];
trl=np.load(sys.argv[2]); trl=trl[trl.files[0]];
dv=np.load(sys.argv[3]);  dv=dv[dv.files[0]];
dvl=np.load(sys.argv[4]); dvl=dvl[dvl.files[0]];

# normalizamos las características en [-1,1]
S=max(tr.max(),abs(tr.min())); tr/=S; dv/=S;

# probamos diferentes valores para el parámetro de penalización C, C>0,
# y hallamos el error en tr y dv para cada uno de ellos
for C in [1e-2, 1e-1, 1, 1e1]:
  print(f'{C}',end='')
  for G in [1, 10, 20]:
    clf=svm.SVC(kernel='sigmoid', C=C, gamma=G).fit(tr, trl)
    etr=(trl!=clf.predict(tr)).mean();
    edv=(dvl!=clf.predict(dv)).mean()*100;
    print(f'\t{edv:4.2f}',end='');
  print()
