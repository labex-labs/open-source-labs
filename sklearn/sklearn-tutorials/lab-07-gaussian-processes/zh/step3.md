# 高斯过程分类（GPC）

GaussianProcessClassifier 类实现了用于概率分类的 GPC。它在一个潜在函数上放置一个高斯过程先验，然后通过一个链接函数进行压缩以获得类别概率。GPC 通过执行一对其余或一对一的训练和预测来支持多类别分类。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

X = np.linspace(0, 10, 100).reshape(-1, 1)
y = np.sin(X).ravel() + np.random.normal(0, 0.1, X.shape[0])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.gaussian_process import GaussianProcessClassifier
# 创建一个具有 RBF 核的 GPC 模型
kernel = RBF()
model = GaussianProcessClassifier(kernel=kernel)

# 将模型拟合到训练数据
model.fit(X_train, y_train)

# 使用训练好的模型进行预测
y_pred = model.predict(X_test)
```
