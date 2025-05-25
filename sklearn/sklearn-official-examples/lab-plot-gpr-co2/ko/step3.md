# 모델 적합 및 외삽

이제 가우시안 프로세스 회귀자를 사용하여 사용 가능한 데이터를 적합할 준비가 되었습니다. 문헌의 예제를 따르기 위해 대상에서 평균을 뺍니다. 1958 년부터 현재 달까지의 가상 데이터를 생성하고, 가우시안 프로세스를 사용하여 학습 데이터에 대한 예측을 수행하여 적합도를 검사하고, 미래 데이터를 사용하여 모델이 수행하는 외삽을 확인합니다.

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
plt.xlabel("연도")
plt.ylabel("CO$_2$ 농도의 월 평균 (ppm)")
plt.title(
    "마우나 로아 천문대의 공기 샘플 측정치의 월 평균"
)
plt.show()
```
