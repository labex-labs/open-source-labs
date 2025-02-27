# Trainieren und Evaluieren des überwachten Modells

In diesem Schritt teilen wir den Datensatz in Trainings- und Testsets auf und trainieren und evaluieren dann die Pipeline für das überwachte Modell, die wir in Schritt 2 erstellt haben.

```python
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

# Teilen des Datensatzes in Trainings- und Testsets
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Trainieren und Evaluieren der Pipeline für das überwachte Modell
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print(
    "Micro-averaged F1 score on test set: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```
