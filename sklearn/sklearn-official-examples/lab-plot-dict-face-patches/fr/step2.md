# Apprendre le dictionnaire d'images

Nous utilisons MiniBatchKMeans pour apprendre le dictionnaire d'images. Nous définissons le nombre de clusters sur 81, définissons un état aléatoire et activons le mode verbeux. Nous créons ensuite un tampon pour stocker les patches et parcourons chaque image dans l'ensemble de données. Nous extrayons 50 patches de chaque image et redimensionnons les données. Nous ajoutons ensuite les données au tampon et incrémentons l'index. Si l'index est un multiple de 10, nous concaténons le tampon et exécutons partial_fit sur les données. Si l'index est un multiple de 100, nous affichons un message indiquant le nombre de patches qui ont été ajustés jusqu'à présent.

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
