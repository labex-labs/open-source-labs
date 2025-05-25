# 이산 SAMME 및 실제 SAMME.R 을 사용한 AdaBoost

이제 이산 및 실제 AdaBoost 분류기를 정의하고 학습 데이터 세트에 맞춥니다.

```python
from sklearn.ensemble import AdaBoostClassifier

ada_discrete = AdaBoostClassifier(
    estimator=dt_stump,
    learning_rate=learning_rate,
    n_estimators=n_estimators,
    algorithm="SAMME",
)
ada_discrete.fit(X_train, y_train)

ada_real = AdaBoostClassifier(
    estimator=dt_stump,
    learning_rate=learning_rate,
    n_estimators=n_estimators,
    algorithm="SAMME.R",
)
ada_real.fit(X_train, y_train)
```
