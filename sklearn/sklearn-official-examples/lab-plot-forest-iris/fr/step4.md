# Définition des modèles

Dans cette étape, nous allons définir les modèles à utiliser pour tracer les surfaces de décision sur l'ensemble de données iris.

```python
models = [
    DecisionTreeClassifier(max_depth=None),
    RandomForestClassifier(n_estimators=n_estimators),
    ExtraTreesClassifier(n_estimators=n_estimators),
    AdaBoostClassifier(DecisionTreeClassifier(max_depth=3), n_estimators=n_estimators),
]
```
