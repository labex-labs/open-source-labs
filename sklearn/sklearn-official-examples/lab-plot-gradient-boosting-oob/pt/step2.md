# Ajustar o Classificador com Estimativas OOB

Em seguida, criaremos um Classificador de Reforço Gradiente com estimativas OOB usando a classe `GradientBoostingClassifier` do módulo `sklearn.ensemble`. Definiremos o número de estimadores para 100 e a taxa de aprendizado para 0,1.

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
