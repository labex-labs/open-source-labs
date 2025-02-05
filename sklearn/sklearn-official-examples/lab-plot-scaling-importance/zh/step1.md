# 加载并准备数据

我们将从scikit-learn中加载葡萄酒数据集，并将其拆分为训练集和测试集。我们还将使用scikit-learn预处理模块中的StandardScaler对训练集中的特征进行缩放。

```python
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X, y = load_wine(return_X_y=True, as_frame=True)
scaler = StandardScaler().set_output(transform="pandas")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)
scaled_X_train = scaler.fit_transform(X_train)
```
