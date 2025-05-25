# Criar um Conjunto de Dados Separável de Duas Classes

Para criar um conjunto de dados separável de duas classes, utilizaremos a função `make_blobs()` do scikit-learn. Esta função gera blobs gaussianos isotrópicos para agrupamento e classificação. Criaremos 40 amostras com dois centros e uma semente aleatória de 6. Também plotaremos os pontos de dados utilizando `matplotlib`.

```python
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# criar um conjunto de dados separável de duas classes
X, y = make_blobs(n_samples=40, centers=2, random_state=6)

# plotar os pontos de dados
plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=plt.cm.Paired)
plt.show()
```
