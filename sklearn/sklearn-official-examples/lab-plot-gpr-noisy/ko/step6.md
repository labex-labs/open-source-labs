# 데이터 시각화

이 단계에서는 가우시안 프로세스 회귀 모델이 예측한 결과를 시각화합니다.

```python
plt.plot(X, y, label="예상 신호")
plt.scatter(x=X_train[:, 0], y=y_train, color="black", alpha=0.4, label="관측값")
plt.errorbar(X, y_mean, y_std)
plt.legend()
plt.xlabel("X")
plt.ylabel("y")
_ = plt.title(
    (
        f"초기: {kernel}\n최적: {gpr.kernel_}\n로그 - 주변확률밀도: "
        f"{gpr.log_marginal_likelihood(gpr.kernel_.theta)}"
    ),
    fontsize=8,
)
```
