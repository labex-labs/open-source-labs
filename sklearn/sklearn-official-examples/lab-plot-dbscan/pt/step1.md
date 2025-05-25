# Geração de Dados

Usaremos a função `make_blobs` do módulo `sklearn.datasets` para gerar um conjunto de dados sintético com três clusters. O conjunto de dados consistirá em 750 amostras com um desvio padrão de cluster de 0,4. Também padronizaremos os dados usando o `StandardScaler` do módulo `sklearn.preprocessing`.

```python
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(
    n_samples=750, centers=centers, cluster_std=0.4, random_state=0
)

X = StandardScaler().fit_transform(X)
```
