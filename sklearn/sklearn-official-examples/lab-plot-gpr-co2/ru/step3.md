# Настройка модели и экстраполяция

Теперь мы готовы использовать регрессор с гауссовым процессом и настроить модель на доступные данные. Чтобы следовать примеру из литературы, мы вычтем среднее значение из целевой переменной. Мы создадим синтетические данные с 1958 года по текущий месяц и используем гауссовый процесс для предсказания на обучающих данных, чтобы проверить качество настройки, и на будущих данных, чтобы увидеть, как модель выполняет экстраполяцию.

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
