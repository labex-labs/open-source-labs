# Crear y entrenar los modelos

Crearemos dos modelos de AdaBoost, uno que utilice SAMME y el otro que utilice SAMME.R. Ambos modelos utilizarán DecisionTreeClassifier con una profundidad máxima de 2 y 300 estimadores.

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
