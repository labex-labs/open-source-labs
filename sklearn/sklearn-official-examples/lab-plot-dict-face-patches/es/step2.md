# Aprender el diccionario de imágenes

Utilizamos MiniBatchKMeans para aprender el diccionario de imágenes. Establecemos el número de clusters en 81, configuramos un estado aleatorio y habilitamos el modo detallado. Luego creamos un búfer para almacenar los parches y recorremos cada imagen del conjunto de datos. Extraemos 50 parches de cada imagen y rediseñamos los datos. A continuación, agregamos los datos al búfer e incrementamos el índice. Si el índice es múltiplo de 10, concatenamos el búfer y ejecutamos partial_fit en los datos. Si el índice es múltiplo de 100, imprimimos un mensaje indicando el número de parches que se han ajustado hasta el momento.

```python
import time
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.feature_extraction.image import extract_patches_2d

print("Learning the dictionary... ")
rng = np.random.RandomState(0)
kmeans = MiniBatchKMeans(n_clusters=81, random_state=rng, verbose=True, n_init=3)
patch_size = (20, 20)

buffer = []
t0 = time.time()

# The online learning part: cycle over the whole dataset 6 times
index = 0
for _ in range(6):
    for img in faces.images:
        data = extract_patches_2d(img, patch_size, max_patches=50, random_state=rng)
        data = np.reshape(data, (len(data), -1))
        buffer.append(data)
        index += 1
        if index % 10 == 0:
            data = np.concatenate(buffer, axis=0)
            data -= np.mean(data, axis=0)
            data /= np.std(data, axis=0)
            kmeans.partial_fit(data)
            buffer = []
        if index % 100 == 0:
            print("Partial fit of %4i out of %i" % (index, 6 * len(faces.images)))

dt = time.time() - t0
print("done in %.2fs." % dt)
```
