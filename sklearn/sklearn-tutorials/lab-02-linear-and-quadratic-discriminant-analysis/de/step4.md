# Durchführen einer Dimensionsreduktion mit LDA

LDA kann auch für eine überwachte Dimensionsreduktion (supervised dimensionality reduction) verwendet werden. Wir werden dies demonstrieren, indem wir die Dimension des Iris-Datensatzes reduzieren.

```python
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Perform dimensionality reduction using LDA
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X, y)
```
