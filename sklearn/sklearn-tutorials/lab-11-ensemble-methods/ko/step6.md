# 랜덤 포레스트 분류기 학습

다음으로, 학습 데이터에 랜덤 포레스트 분류기를 적용합니다. 랜덤 포레스트 분류기도 부트스트랩 샘플링을 사용하여 여러 개의 의사결정 트리를 생성하는 앙상블 방법이지만, 각 분할에서 특징의 부분 집합만 고려하여 추가적인 무작위성을 더합니다.

```python
random_forest = RandomForestClassifier(n_estimators=10)
random_forest.fit(X_train, y_train)
```
