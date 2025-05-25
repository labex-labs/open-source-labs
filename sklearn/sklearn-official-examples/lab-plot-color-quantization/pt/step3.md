# Ajustar o Modelo K-Means

Ajustaremos o modelo K-Means a uma pequena amostra dos dados da imagem e usá-lo-emos para prever os índices de cores na imagem completa.

```python
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
from time import time

n_colors = 64

# Ajustar o modelo K-Means a uma pequena amostra dos dados
print("Ajustando o modelo a uma pequena amostra dos dados")
t0 = time()
image_array_sample = shuffle(image_array, random_state=0, n_samples=1000)
kmeans = KMeans(n_clusters=n_colors, n_init="auto", random_state=0).fit(
    image_array_sample
)
print(f"feito em {time() - t0:0.3f}s.")

# Obter rótulos para todos os pontos
print("Prevendo índices de cores na imagem completa (k-means)")
t0 = time()
labels = kmeans.predict(image_array)
print(f"feito em {time() - t0:0.3f}s.")
```
