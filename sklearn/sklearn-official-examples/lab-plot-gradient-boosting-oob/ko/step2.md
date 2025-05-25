# OOB 추정치를 사용한 분류기 적합

다음으로 `sklearn.ensemble` 모듈의 `GradientBoostingClassifier` 클래스를 사용하여 OOB 추정치를 사용한 Gradient Boosting 분류기를 생성합니다. 추정자 수는 100 으로, 학습률은 0.1 로 설정합니다.

```python
from sklearn.ensemble import GradientBoostingClassifier

params = {
    "n_estimators": 100,
    "learning_rate": 0.1,
    "subsample": 1.0,
    "max_depth": 3,
    "min_samples_leaf": 1,
    "random_state": 1,
    "oob_score": True
}

clf = GradientBoostingClassifier(**params)
clf.fit(X, y)
```
