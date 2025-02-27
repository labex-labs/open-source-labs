# Инициализация VotingClassifier

Затем мы инициализируем VotingClassifier с мягким голосованием с весами `[1, 1, 5]`, что означает, что при вычислении усреднённой вероятности предсказанные вероятности RandomForestClassifier учитываются в пять раз больше, чем веса других классификаторов.

```python
eclf = VotingClassifier(
    estimators=[("lr", clf1), ("rf", clf2), ("gnb", clf3)],
    voting="soft",
    weights=[1, 1, 5],
)
```
