# モデルのフィッティングと外挿

ここで、ガウス過程回帰器を使用して利用可能なデータにフィッティングする準備が整いました。文献の例に従い、目的変数から平均を引きます。1958 年から現在の月までの合成データを作成し、ガウス過程を使用して訓練データで予測してフィットの良さを検査し、モデルによる外挿を確認するために将来のデータを使用します。

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
