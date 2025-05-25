# AdaBoost 의사결정 트리 생성 및 학습

이 단계에서는 `sklearn.ensemble` 모듈의 `AdaBoostClassifier` 클래스를 사용하여 AdaBoost 의사결정 트리를 생성합니다. 의사결정 트리를 기본 추정기로 사용하고 `max_depth` 매개변수를 1 로 설정합니다. 또한 `algorithm` 매개변수를 "SAMME"로, `n_estimators` 매개변수를 200 으로 설정합니다. 마지막으로, 분류기를 데이터셋에 맞춥니다.

```python
bdt = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=1), algorithm="SAMME", n_estimators=200
)

bdt.fit(X, y)
```
