# Entraîner et évaluer le modèle supervisé

Dans cette étape, nous allons diviser l'ensemble de données en ensembles d'entraînement et de test, puis entraîner et évaluer le pipeline de modèle supervisé que nous avons créé dans l'Étape 2.

```python
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

# Diviser l'ensemble de données en ensembles d'entraînement et de test
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Entraîner et évaluer le pipeline de modèle supervisé
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print(
    "Micro-averaged F1 score on test set: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```
