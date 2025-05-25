# 귀납적 학습 모델 선언

이 단계에서는 알 수 없는 인스턴스에 대한 클러스터 멤버십을 예측하는 데 사용될 귀납적 학습 모델을 선언합니다. scikit-learn 의 `RandomForestClassifier`를 분류기로 사용합니다.

```python
classifier = RandomForestClassifier(random_state=42)
inductive_learner = InductiveClusterer(clusterer, classifier).fit(X)
```
