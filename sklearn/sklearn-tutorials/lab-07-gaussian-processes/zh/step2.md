# GPR 示例

带有噪声水平估计的 GPR：此示例展示了使用包含 WhiteKernel 的和核的 GPR，用于估计数据的噪声水平。

```python
from sklearn.gaussian_process.kernels import WhiteKernel

# 创建一个具有 RBF 核和 WhiteKernel 的 GPR 模型
kernel = RBF() + WhiteKernel()
model = GaussianProcessRegressor(kernel=kernel)

# 将模型拟合到训练数据
model.fit(X_train, y_train)

# 使用训练好的模型进行预测
y_pred = model.predict(X_test)
```

GPR 与核岭回归的比较：核岭回归（KRR）和 GPR 都使用“核技巧”来学习目标函数。GPR 学习一个生成式概率模型并能提供置信区间，而 KRR 仅提供预测。

```python
from sklearn.kernel_ridge import KernelRidge

# 创建一个核岭回归模型
krr_model = KernelRidge(kernel='rbf')

# 将 KRR 模型拟合到训练数据
krr_model.fit(X_train, y_train)

# 使用 KRR 模型进行预测
krr_y_pred = krr_model.predict(X_test)

# 将结果与 GPR 进行比较
gpr_model = GaussianProcessRegressor(kernel=RBF())
gpr_model.fit(X_train, y_train)
gpr_y_pred = gpr_model.predict(X_test)
```

莫纳罗亚二氧化碳数据上的 GPR：此示例展示了使用对数边际似然上的梯度上升进行复杂的核工程和超参数优化。数据由夏威夷莫纳罗亚天文台收集的每月平均大气二氧化碳浓度组成。目标是将二氧化碳浓度建模为时间的函数。

```python
from sklearn.gaussian_process.kernels import RBF, ExpSineSquared, RationalQuadratic, WhiteKernel

# 创建一个具有复合核的 GPR 模型
kernel = 34.4**2 * RBF(length_scale=41.8) + 3.27**2 * RBF(length_scale=180) * ExpSineSquared(length_scale=1.44, periodicity=1) + 0.446**2 * RationalQuadratic(alpha=17.7, length_scale=0.957) + 0.197**2 * RBF(length_scale=0.138) + WhiteKernel(noise_level=0.0336)
model = GaussianProcessRegressor(kernel=kernel)

# 将模型拟合到数据
model.fit(X_train, y_train)

# 使用训练好的模型进行预测
y_pred = model.predict(X_test)
```
