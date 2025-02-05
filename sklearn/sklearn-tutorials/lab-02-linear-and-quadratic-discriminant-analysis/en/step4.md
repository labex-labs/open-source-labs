# Perform dimensionality reduction using LDA

LDA can also be used for supervised dimensionality reduction. We will demonstrate this by reducing the dimension of the Iris dataset.

```python
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Perform dimensionality reduction using LDA
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X, y)
```
