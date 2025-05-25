# Reduzir a dimensionalidade usando LDA

O LDA também pode ser usado para redução de dimensionalidade supervisionada. Vamos demonstrar isso reduzindo a dimensão do conjunto de dados Iris.

```python
from sklearn.datasets import load_iris

# Carregar o conjunto de dados Iris
iris = load_iris()
X, y = iris.data, iris.target

# Reduzir a dimensionalidade usando LDA
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X, y)
```
