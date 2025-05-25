# Carregar os Dados

Carregaremos o conjunto de dados de íris utilizando o módulo `datasets` do Scikit-Learn. Utilizaremos apenas duas características: comprimento da sépala e comprimento da pétala.

```python
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data[:, [0, 2]]
y = iris.target
```
