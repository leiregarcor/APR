import numpy as np
#sirve para comprobar los ficheros obtenidos con part.py pero no hace falta hacerlo
z=np.load('tr.npz')
print(z.files)
print(z['dat'].shape)