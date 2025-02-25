# Lecture de tableaux à partir du disque

Vous pouvez lire des tableaux à partir du disque dans différents formats. Pour les formats binaires standards, il existe des bibliothèques Python telles que h5py pour HDF5 et Astropy pour FITS. Pour les formats ASCII courants comme CSV et TSV, vous pouvez utiliser les fonctions `np.loadtxt` et `np.genfromtxt`. Voici un exemple de lecture d'un fichier CSV :

```python
import numpy as np

data = np.loadtxt('data.csv', delimiter=',', skiprows=1)
```
