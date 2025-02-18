# LDA を使用した次元削減を行う

LDA は教師付き次元削減にも使用できます。ここでは、アヤメ (Iris) データセットの次元を削減することでそれを実証します。

```python
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Perform dimensionality reduction using LDA
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X, y)
```
