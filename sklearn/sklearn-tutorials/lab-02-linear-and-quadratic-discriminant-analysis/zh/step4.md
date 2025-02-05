# 使用 LDA 进行降维

LDA 还可用于有监督的降维。我们将通过降低鸢尾花数据集的维度来演示这一点。

```python
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Perform dimensionality reduction using LDA
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X, y)
```
