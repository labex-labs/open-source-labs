# Создаём и обучаем модели

Мы создадим две модели AdaBoost, одну с использованием SAMME и другую с использованием SAMME.R. обе модели будут использовать DecisionTreeClassifier с максимальной глубиной 2 и 300 оценщиками.

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
