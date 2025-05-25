# Carregar o Conjunto de Dados

O primeiro passo é carregar o conjunto de dados iris do scikit-learn.

```python
from sklearn.datasets import load_iris

# Carregar o conjunto de dados
iris = load_iris()
X_iris = iris.data
y_iris = iris.target
```
