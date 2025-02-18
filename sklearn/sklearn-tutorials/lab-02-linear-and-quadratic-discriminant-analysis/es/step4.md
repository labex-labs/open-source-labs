# Realizar reducción de dimensionalidad utilizando LDA

El Análisis Discriminante Lineal (LDA) también se puede utilizar para la reducción de dimensionalidad supervisada. Demostraremos esto reduciendo la dimensión del conjunto de datos Iris.

```python
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Perform dimensionality reduction using LDA
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X, y)
```
