# 加载泰坦尼克号数据集

接下来，我们将加载泰坦尼克号数据集，以演示如何使用`compose.ColumnTransformer`和异构数据来使用`set_output`。

```python
from sklearn.datasets import fetch_openml

X, y = fetch_openml(
    "titanic", version=1, as_frame=True, return_X_y=True, parser="pandas"
)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)
```
