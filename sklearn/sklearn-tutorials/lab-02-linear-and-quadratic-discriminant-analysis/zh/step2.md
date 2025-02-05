# 生成合成数据

接下来，我们将生成合成数据，以展示 LDA 和 QDA 之间的差异。我们将使用 scikit-learn 中的 `make_classification` 函数来创建具有不同模式的两个类别。

```python
from sklearn.datasets import make_classification

# Generate synthetic data
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, n_classes=2, random_state=1)
```
