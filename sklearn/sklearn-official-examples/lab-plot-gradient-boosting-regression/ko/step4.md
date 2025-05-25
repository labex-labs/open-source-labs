# 학습 편차 시각화

마지막으로, 결과를 시각화합니다. 이를 위해 먼저 테스트 세트의 편차를 계산한 다음, 부스팅 반복 횟수에 따른 편차를 플롯합니다.

```python
test_score = np.zeros((params["n_estimators"],), dtype=np.float64)
for i, y_pred in enumerate(reg.staged_predict(X_test)):
    test_score[i] = mean_squared_error(y_test, y_pred)

fig = plt.figure(figsize=(6, 6))
plt.subplot(1, 1, 1)
plt.title("편차")
plt.plot(
    np.arange(params["n_estimators"]) + 1,
    reg.train_score_,
    "b-",
    label="훈련 세트 편차",
)
plt.plot(
    np.arange(params["n_estimators"]) + 1, test_score, "r-", label="테스트 세트 편차"
)
plt.legend(loc="upper right")
plt.xlabel("부스팅 반복 횟수")
plt.ylabel("편차")
fig.tight_layout()
plt.show()
```
