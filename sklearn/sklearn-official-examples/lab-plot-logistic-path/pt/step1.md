# Carregar o conjunto de dados Iris

Vamos carregar o conjunto de dados Iris da biblioteca scikit-learn. O conjunto de dados contém quatro características: Comprimento da sépala, Largura da sépala, Comprimento da pétala e Largura da pétala. Usaremos apenas as duas primeiras características para classificação binária.

```python
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
y = iris.target

X = X[y != 2] # Use only first two features for binary classification
y = y[y != 2]

X /= X.max() # Normalize X to speed-up convergence
```
