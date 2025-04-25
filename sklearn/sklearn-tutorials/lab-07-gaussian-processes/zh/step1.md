# 高斯过程回归（GPR）

GaussianProcessRegressor 类实现了用于回归任务的高斯过程。它需要为高斯过程指定一个先验，例如均值和协方差函数。核的超参数在拟合过程中进行优化。下面来看一个使用 GPR 进行回归的示例。

```python
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF

# 创建一个具有 RBF 核的 GPR 模型
kernel = RBF()
model = GaussianProcessRegressor(kernel=kernel)

# 将模型拟合到训练数据
model.fit(X_train, y_train)

# 使用训练好的模型进行预测
y_pred = model.predict(X_test)
```
