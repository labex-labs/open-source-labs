# 회귀 모델 학습

이제 Gradient Boosting 회귀 모델, Random Forest 회귀 모델, 그리고 선형 회귀 모델을 초기화합니다. 다음으로, 이 세 가지 회귀 모델을 사용하여 투표 회귀 모델 (Voting Regressor) 을 생성합니다.

```python
# 분류기 학습
reg1 = GradientBoostingRegressor(random_state=1)
reg2 = RandomForestRegressor(random_state=1)
reg3 = LinearRegression()

reg1.fit(X, y)
reg2.fit(X, y)
reg3.fit(X, y)

ereg = VotingRegressor([("gb", reg1), ("rf", reg2), ("lr", reg3)])
ereg.fit(X, y)
```
