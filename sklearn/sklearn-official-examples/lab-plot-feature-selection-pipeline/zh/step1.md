# 生成并分割数据集

我们将首先使用 Scikit-learn 的`make_classification`函数生成一个二元分类数据集。我们还将使用 Scikit-learn 的`train_test_split`函数将数据集拆分为训练子集和测试子集。

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_features=20,
    n_informative=3,
    n_redundant=0,
    n_classes=2,
    n_clusters_per_class=2,
    random_state=42,
)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
```
