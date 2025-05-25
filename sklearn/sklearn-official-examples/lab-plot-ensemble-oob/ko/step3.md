# 앙상블 분류기 정의

`max_features` 매개변수의 값이 다른 세 개의 랜덤 포레스트 분류기를 리스트로 정의합니다. 학습 중 OOB 오류율 추적을 위해 `warm_start` 생성 매개변수를 `True`로 설정합니다. 또한 OOB 오류율 계산을 위해 `oob_score` 매개변수를 `True`로 설정합니다.

```python
ensemble_clfs = [
    (
        "RandomForestClassifier, max_features='sqrt'",
        RandomForestClassifier(
            warm_start=True,
            oob_score=True,
            max_features="sqrt",
            random_state=RANDOM_STATE,
        ),
    ),
    (
        "RandomForestClassifier, max_features='log2'",
        RandomForestClassifier(
            warm_start=True,
            max_features="log2",
            oob_score=True,
            random_state=RANDOM_STATE,
        ),
    ),
    (
        "RandomForestClassifier, max_features=None",
        RandomForestClassifier(
            warm_start=True,
            max_features=None,
            oob_score=True,
            random_state=RANDOM_STATE,
        ),
    ),
]
```
