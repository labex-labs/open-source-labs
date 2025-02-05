# 高斯过程分类（GPC）

GaussianProcessClassifier类实现了用于概率分类的GPC。它在一个潜在函数上放置一个高斯过程先验，然后通过一个链接函数进行压缩以获得类别概率。GPC通过执行一对其余或一对一的训练和预测来支持多类别分类。

```python
from sklearn.gaussian_process import GaussianProcessClassifier

# 创建一个具有RBF核的GPC模型
kernel = RBF()
model = GaussianProcessClassifier(kernel=kernel)

# 将模型拟合到训练数据
model.fit(X_train, y_train)

# 使用训练好的模型进行预测
y_pred = model.predict(X_test)
```
