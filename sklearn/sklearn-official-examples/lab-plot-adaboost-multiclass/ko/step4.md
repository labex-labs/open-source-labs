# 모델 생성 및 학습

SAMME 와 SAMME.R 를 사용하는 두 개의 AdaBoost 모델을 생성합니다. 두 모델 모두 DecisionTreeClassifier 를 사용하며, 최대 깊이 (max depth) 는 2 이고 추정자 (estimators) 는 300 개입니다.

```python
bdt_real = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=2), n_estimators=300, learning_rate=1
)

bdt_discrete = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=2),
    n_estimators=300,
    learning_rate=1.5,
    algorithm="SAMME",
)

bdt_real.fit(X_train, y_train)
bdt_discrete.fit(X_train, y_train)
```
