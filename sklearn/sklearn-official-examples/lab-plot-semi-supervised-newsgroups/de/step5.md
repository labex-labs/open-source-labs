# Trainiere und bewerte das Self-Training-Modell

In diesem Schritt werden wir Self-Training auf 20% der markierten Daten anwenden. Wir werden 20% der markierten Daten zufällig auswählen, das Modell auf diesen Daten trainieren und dann das Modell verwenden, um die Labels für die verbleibenden unmarkierten Daten vorherzusagen.

```python
import numpy as np

# Wähle 20% der Trainingsdaten
y_mask = np.random.rand(len(y_train)) < 0.2
X_20, y_20 = map(
    list, zip(*((x, y) for x, y, m in zip(X_train, y_train, y_mask) if m))
)

# Setze den nicht maskierten Teilsatz als unmarkiert
y_train[~y_mask] = -1

# Trainiere und bewerte die Self-Training-Pipeline
st_pipeline.fit(X_train, y_train)
y_pred = st_pipeline.predict(X_test)
print(
    "Mikro-aggregierter F1-Score auf dem Testset: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```