# 加载数据集

我们将使用 scikit-learn 的`fetch_california_housing`函数加载加利福尼亚住房数据集。该数据集包含 20,640 个样本和 8 个特征。

```python
from sklearn.datasets import fetch_california_housing

X, y = fetch_california_housing(return_X_y=True, as_frame=True)
n_samples, n_features = X.shape

print(f"The dataset consists of {n_samples} samples and {n_features} features")
```
