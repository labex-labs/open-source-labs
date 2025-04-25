# 模型拟合与外推

现在，我们准备好使用高斯过程回归器并拟合可用数据。为了遵循文献中的示例，我们将从目标值中减去均值。我们创建从 1958 年到当前月份的合成数据，并使用高斯过程对训练数据进行预测以检查拟合优度，对未来数据进行预测以查看模型的外推效果。

```python
from sklearn.gaussian_process import GaussianProcessRegressor
import datetime
import numpy as np
import matplotlib.pyplot as plt

y_mean = y.mean()
gaussian_process = GaussianProcessRegressor(kernel=co2_kernel, normalize_y=False)
gaussian_process.fit(X, y - y_mean)

today = datetime.datetime.now()
current_month = today.year + today.month / 12
X_test = np.linspace(start=1958, stop=current_month, num=1_000).reshape(-1, 1)
mean_y_pred, std_y_pred = gaussian_process.predict(X_test, return_std=True)
mean_y_pred += y_mean

plt.plot(X, y, color="black", linestyle="dashed", label="Measurements")
plt.plot(X_test, mean_y_pred, color="tab:blue", alpha=0.4, label="Gaussian process")
plt.fill_between(
    X_test.ravel(),
    mean_y_pred - std_y_pred,
    mean_y_pred + std_y_pred,
    color="tab:blue",
    alpha=0.2,
)
plt.legend()
plt.xlabel("Year")
plt.ylabel("Monthly average of CO$_2$ concentration (ppm)")
plt.title(
    "Monthly average of air samples measurements\nfrom the Mauna Loa Observatory"
)
plt.show()
```
