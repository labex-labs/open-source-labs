# 데이터 시각화

이 단계에서는 예상 신호와 함께 노이즈가 추가된 학습 데이터셋을 시각화합니다.

```python
plt.plot(X, y, label="예상 신호")
plt.scatter(
    x=X_train[:, 0],
    y=y_train,
    color="black",
    alpha=0.4,
    label="관측값",
)
plt.legend()
plt.xlabel("X")
_ = plt.ylabel("y")
```
