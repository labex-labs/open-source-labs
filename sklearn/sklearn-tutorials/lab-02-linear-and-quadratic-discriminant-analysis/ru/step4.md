# Выполнение понижения размерности с использованием LDA

LDA также может быть использован для контролируемого (с учителем) понижения размерности. Мы продемонстрируем это, понизив размерность набора данных Iris.

```python
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Perform dimensionality reduction using LDA
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X, y)
```
