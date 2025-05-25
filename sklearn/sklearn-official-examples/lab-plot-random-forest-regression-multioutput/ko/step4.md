# 랜덤 포레스트 회귀 모델 생성

scikit-learn 의 `RandomForestRegressor`를 사용하여 최대 깊이 30, 추정자 100 개를 가진 랜덤 포레스트 회귀 모델을 생성합니다.

```python
max_depth = 30
regr_rf = RandomForestRegressor(n_estimators=100, max_depth=max_depth, random_state=2)
regr_rf.fit(X_train, y_train)
```
