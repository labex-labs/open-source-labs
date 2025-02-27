# Trainieren und Evaluieren des Self-Training-Modells

In diesem Schritt verwenden wir Self-Training auf 20 % der gelabelten Daten. Wir wählen zufällig 20 % der gelabelten Daten aus, trainieren das Modell auf diesen Daten und verwenden dann das Modell, um Labels für die verbleibenden ungelabelten Daten vorherzusagen.

```python
import numpy as np

# Auswahl von 20 % der Trainingsdaten
y_mask = np.random.rand(len(y_train)) < 0.2
X_20, y_20 = map(
    list, zip(*((x, y) for x, y, m in zip(X_train, y_train, y_mask) if m))
)

# Setzen der nicht markierten Teilmenge auf ungelabelt
y_train[~y_mask] = -1

# Trainieren und Evaluieren der Self-Training-Pipeline
st_pipeline.fit(X_train, y_train)
y_pred = st_pipeline.predict(X_test)
print(
    "Micro-averaged F1 score on test set: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```
