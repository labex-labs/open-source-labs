# Trainiere und计算 die bewertete überwachte Modell

In diesem Schritt werden wir das Dataset in Trainings- und Testsets unterteilen und anschließend das in Schritt 2 erstellte Pipeline-Modell für das überwachte Lernen trainieren und bewerten.

```python
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

# Teile das Dataset in Trainings- und Testsets auf
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Trainiere und berechne die bewertete überwachte Modell-Pipeline
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print(
    "Mikro-aggregierter F1-Score auf dem Testset: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```