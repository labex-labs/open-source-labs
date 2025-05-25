# Função de Predição de Valores Discrepantes

O próximo passo é definir uma função de previsão de valores discrepantes. Neste exemplo, usamos os algoritmos `LocalOutlierFactor` e `IsolationForest`. A função `compute_prediction` retorna a pontuação média de valores discrepantes de X.

```python
from sklearn.neighbors import LocalOutlierFactor
from sklearn.ensemble import IsolationForest

def compute_prediction(X, model_name):
    print(f"Computando previsão de {model_name}...")
    if model_name == "LOF":
        clf = LocalOutlierFactor(n_neighbors=20, contamination="auto")
        clf.fit(X)
        y_pred = clf.negative_outlier_factor_
    if model_name == "IForest":
        clf = IsolationForest(random_state=rng, contamination="auto")
        y_pred = clf.fit(X).decision_function(X)
    return y_pred
```
