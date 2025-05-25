# Gerar dados de amostra

Geramos os dados de amostra utilizando a função `make_checkerboard`. Cada pixel dentro de `shape=(300, 300)` representa, com sua cor, um valor de uma distribuição uniforme. O ruído é adicionado a partir de uma distribuição normal, onde o valor escolhido para `noise` é o desvio padrão.

```python
from sklearn.datasets import make_checkerboard
from matplotlib import pyplot as plt

n_clusters = (4, 3)
data, rows, columns = make_checkerboard(
    shape=(300, 300), n_clusters=n_clusters, noise=10, shuffle=False, random_state=42
)

plt.matshow(data, cmap=plt.cm.Blues)
plt.title("Conjunto de dados original")
_ = plt.show()
```
