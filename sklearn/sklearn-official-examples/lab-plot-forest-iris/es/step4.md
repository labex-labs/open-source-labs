# Definir modelos

En este paso, definiremos los modelos que se utilizarán para trazar las superficies de decisión en el conjunto de datos iris.

```python
models = [
    DecisionTreeClassifier(max_depth=None),
    RandomForestClassifier(n_estimators=n_estimators),
    ExtraTreesClassifier(n_estimators=n_estimators),
    AdaBoostClassifier(DecisionTreeClassifier(max_depth=3), n_estimators=n_estimators),
]
```
