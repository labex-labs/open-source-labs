# 매개변수 공간 정의

탐색할 하이퍼파라미터와 해당 값을 포함하는 딕셔너리 `param_dist`를 정의합니다. 하이퍼파라미터는 `max_depth`, `max_features`, `min_samples_split`, `bootstrap`, 그리고 `criterion`입니다. `max_features`와 `min_samples_split`의 탐색 범위는 `scipy.stats` 모듈의 `randint` 함수를 사용하여 정의합니다. 매개변수 공간을 정의하는 코드는 다음과 같습니다.

```python
param_dist = {
    "max_depth": [3, None],
    "max_features": randint(1, 6),
    "min_samples_split": randint(2, 11),
    "bootstrap": [True, False],
    "criterion": ["gini", "entropy"],
}
```
