# 데이터셋 시각화

데이터셋과 잔차 `y - mean(y)`의 분포를 시각화할 것입니다.

```python
import matplotlib.pyplot as plt

_, axs = plt.subplots(nrows=2, ncols=2, figsize=(15, 11), sharex="row", sharey="row")

axs[0, 0].plot(x, y_true_mean, label="True mean")
axs[0, 0].scatter(x, y_normal, color="black", alpha=0.5, label="Observations")
axs[1, 0].hist(y_true_mean - y_normal, edgecolor="black")

axs[0, 1].plot(x, y_true_mean, label="True mean")
axs[0, 1].scatter(x, y_pareto, color="black", alpha=0.5, label="Observations")
axs[1, 1].hist(y_true_mean - y_pareto, edgecolor="black")

axs[0, 0].set_title("이종분산 정규 분포를 갖는 대상 데이터셋")
axs[0, 1].set_title("비대칭 파레토 분포를 갖는 대상 데이터셋")
axs[1, 0].set_title(
    "이종분산 정규 분포를 갖는 대상 데이터셋의 잔차 분포"
)
axs[1, 1].set_title("비대칭 파레토 분포를 갖는 대상 데이터셋의 잔차 분포")
axs[0, 0].legend()
axs[0, 1].legend()
axs[0, 0].set_ylabel("y")
axs[1, 0].set_ylabel("빈도")
axs[0, 1].set_xlabel("x")
axs[0, 0].set_xlabel("x")
axs[1, 0].set_xlabel("잔차")
_ = axs[1, 1].set_xlabel("잔차")
```
