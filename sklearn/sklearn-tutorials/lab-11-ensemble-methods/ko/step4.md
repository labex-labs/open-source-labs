# Bagging 분류기 학습

이제 학습 데이터에 Bagging 분류기를 적용합니다. Bagging 분류기는 부트스트랩 샘플링을 사용하여 여러 개의 기본 모델 (종종 의사결정 트리) 을 생성하고, 다수결 투표를 통해 그 예측을 집계하는 앙상블 방법입니다.

```python
bagging = BaggingClassifier(DecisionTreeClassifier(), n_estimators=10)
bagging.fit(X_train, y_train)
```
