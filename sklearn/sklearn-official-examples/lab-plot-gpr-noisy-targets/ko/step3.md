# 예측 및 신뢰 구간

모델을 맞춘 후, 커널의 하이퍼파라미터가 최적화되었음을 확인합니다. 이제 전체 데이터 세트의 평균 예측을 계산하고 95% 신뢰 구간을 플롯합니다.

```python
mean_prediction, std_prediction = gaussian_process.predict(X, return_std=True)

plt.plot(X, y, label=r"$f(x) = x \sin(x)$", linestyle="dotted")
plt.scatter(X_train, y_train, label="Observations")
plt.plot(X, mean_prediction, label="Mean prediction")
plt.fill_between(
    X.ravel(),
    mean_prediction - 1.96 * std_prediction,
    mean_prediction + 1.96 * std_prediction,
    alpha=0.5,
    label=r"95% confidence interval",
)
plt.legend()
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
_ = plt.title("잡음 없는 데이터 세트에 대한 가우시안 프로세스 회귀")
```
