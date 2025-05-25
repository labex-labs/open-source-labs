# Huber 회귀 분석 적용

이제 HuberRegressor 를 데이터셋에 적용합니다. epsilon 값의 범위에 걸쳐 모델을 적합시켜 epsilon 값이 증가함에 따라 결정 함수가 Ridge 회귀의 결정 함수에 접근하는 방식을 보여줍니다.

```python
# epsilon 값의 범위 정의
epsilon_values = [1, 1.5, 1.75, 1.9]

# 플롯을 위한 x 값 정의
x = np.linspace(X.min(), X.max(), 7)

# 플롯을 위한 색상 정의
colors = ["r-", "b-", "y-", "m-"]

# 일련의 epsilon 값에 대해 huber 회귀 분석 적용
for k, epsilon in enumerate(epsilon_values):
    huber = HuberRegressor(alpha=0.0, epsilon=epsilon)
    huber.fit(X, y)
    coef_ = huber.coef_ * x + huber.intercept_
    plt.plot(x, coef_, colors[k], label="huber 손실, %s" % epsilon)

# 플롯에 범례 추가
plt.legend(loc=0)

# 플롯 표시
plt.title("다양한 epsilon 값을 갖는 HuberRegressor")
plt.xlabel("X")
plt.ylabel("y")
plt.show()
```
