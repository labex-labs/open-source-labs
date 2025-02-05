# 数据集与模型

我们将使用鸢尾花数据集和线性支持向量分类器（Linear SVC）来区分两种鸢尾花。首先，我们将导入必要的库并加载数据集。

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

X, y = load_iris(return_X_y=True)
```

接下来，我们将向数据集中添加噪声特征，并将其拆分为训练集和测试集。

```python
random_state = np.random.RandomState(0)
n_samples, n_features = X.shape
X = np.concatenate([X, random_state.randn(n_samples, 200 * n_features)], axis=1)

X_train, X_test, y_train, y_test = train_test_split(
    X[y < 2], y[y < 2], test_size=0.5, random_state=random_state
)
```

最后，我们将使用标准缩放器（StandardScaler）对数据进行缩放，并将线性支持向量分类器拟合到训练数据上。

```python
classifier = make_pipeline(
    StandardScaler(), LinearSVC(random_state=random_state, dual="auto")
)
classifier.fit(X_train, y_train)
```
