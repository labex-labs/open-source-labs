# Réduction de dimension à l'aide de l'Analyse Discriminante Linéaire (LDA)

LDA peut également être utilisé pour la réduction de dimension supervisée. Nous allons démontrer cela en réduisant la dimension de l'ensemble de données Iris.

```python
from sklearn.datasets import load_iris

# Chargement de l'ensemble de données Iris
iris = load_iris()
X, y = iris.data, iris.target

# Réduction de dimension à l'aide de LDA
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X, y)
```
