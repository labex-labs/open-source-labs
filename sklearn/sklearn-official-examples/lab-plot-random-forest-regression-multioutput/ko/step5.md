# MultiOutputRegressor 생성

기본 추정기로 랜덤 포레스트 회귀 모델을 사용하는 `MultiOutputRegressor`를 생성합니다. 이전 단계 (4 단계) 와 동일한 매개변수를 사용합니다.

```python
regr_multirf = MultiOutputRegressor(RandomForestRegressor(n_estimators=100, max_depth=max_depth, random_state=0))
regr_multirf.fit(X_train, y_train)
```
