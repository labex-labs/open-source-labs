# Aprender o Dicionário de Imagens

Usamos MiniBatchKMeans para aprender o dicionário de imagens. Definimos o número de clusters para 81, definimos um estado aleatório e ativamos o modo verbose. Em seguida, criamos um buffer para armazenar patches e iteramos sobre cada imagem no conjunto de dados. Extraímos 50 patches de cada imagem e redimensionamos os dados. Em seguida, anexamos os dados ao buffer e incrementamos o índice. Se o índice for um múltiplo de 10, concatenamos o buffer e executamos partial_fit nos dados. Se o índice for um múltiplo de 100, imprimimos uma mensagem indicando o número de patches que foram ajustados até agora.

```python
import time
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.feature_extraction.image import extract_patches_2d

print("Aprendendo o dicionário... ")
rng = np.random.RandomState(0)
kmeans = MiniBatchKMeans(n_clusters=81, random_state=rng, verbose=True, n_init=3)
patch_size = (20, 20)

buffer = []
t0 = time.time()

# A parte de aprendizado online: ciclo sobre todo o conjunto de dados 6 vezes
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
            print("Ajuste parcial de %4i de %i" % (index, 6 * len(faces.images)))

dt = time.time() - t0
print("Concluído em %.2fs." % dt)
```
