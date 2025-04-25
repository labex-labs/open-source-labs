# 加载并准备数据

我们首先加载 Covtype 数据集，并通过仅选择一个类别将其转换为二分类问题。然后，我们将数据划分为训练集和测试集，并对特征进行归一化处理。

```python
from sklearn.datasets import fetch_covtype
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, Normalizer

# 加载 Covtype 数据集，仅选择一个类别
X, y = fetch_covtype(return_X_y=True)
y[y!= 2] = 0
y[y == 2] = 1

# 将数据划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=5000, test_size=10000, random_state=42
)

# 对特征进行归一化处理
mm = make_pipeline(MinMaxScaler(), Normalizer())
X_train = mm.fit_transform(X_train)
X_test = mm.transform(X_test)
```
