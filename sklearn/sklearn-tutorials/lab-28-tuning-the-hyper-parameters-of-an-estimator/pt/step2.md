# Carregar o conjunto de dados

Em seguida, vamos carregar o conjunto de dados com o qual trabalharemos. Podemos usar qualquer conjunto de dados de nossa escolha para este exercício.

```python
from sklearn.datasets import load_iris

# Carregar o conjunto de dados iris
iris = load_iris()

# Dividir os dados em recursos e alvo
X = iris.data
y = iris.target
```
