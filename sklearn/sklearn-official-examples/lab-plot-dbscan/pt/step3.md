# Computar DBSCAN

Usaremos a classe `DBSCAN` do módulo `sklearn.cluster` para calcular os clusters. Definiremos o parâmetro `eps` como 0,3 e o parâmetro `min_samples` como 10. Podemos acessar as etiquetas atribuídas pelo DBSCAN usando o atributo `labels_`. Amostras ruidosas recebem a etiqueta -1. Também calcularemos o número de clusters e o número de pontos ruidosos.

```python
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics

db = DBSCAN(eps=0.3, min_samples=10).fit(X)
labels = db.labels_

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print("Número estimado de clusters: %d" % n_clusters_)
print("Número estimado de pontos ruidosos: %d" % n_noise_)
```
