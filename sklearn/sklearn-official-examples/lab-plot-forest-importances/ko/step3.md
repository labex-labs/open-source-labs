# 랜덤 포레스트 학습

특징 중요도를 계산하기 위해 랜덤 포레스트 분류기를 학습합니다.

```python
feature_names = [f"feature {i}" for i in range(X.shape[1])]
forest = RandomForestClassifier(random_state=0)
forest.fit(X_train, y_train)
```
