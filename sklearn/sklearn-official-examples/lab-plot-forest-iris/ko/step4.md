# 모델 정의

이 단계에서는 아이리스 데이터셋의 결정 경계를 시각화하는 데 사용할 모델들을 정의합니다.

```python
models = [
    DecisionTreeClassifier(max_depth=None),
    RandomForestClassifier(n_estimators=n_estimators),
    ExtraTreesClassifier(n_estimators=n_estimators),
    AdaBoostClassifier(DecisionTreeClassifier(max_depth=3), n_estimators=n_estimators),
]
```
