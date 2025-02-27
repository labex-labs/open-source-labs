# Entfernen von Merkmalen mit geringer Varianz

Die Klasse `VarianceThreshold` in scikit-learn kann verwendet werden, um Merkmale mit geringer Varianz zu entfernen. Merkmale mit geringer Varianz liefern dem Modell typischerweise nicht viel Information. Wir werden demonstrieren, wie `VarianceThreshold` verwendet wird, um Null-Varianz-Merkmale zu entfernen.

```python
from sklearn.feature_selection import VarianceThreshold

X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]

# Initialisiere VarianceThreshold mit einem Schwellenwert von 80% Variabilität
sel = VarianceThreshold(threshold=(.8 * (1 -.8)))

# Wähle Merkmale mit hoher Variabilität
X_selected = sel.fit_transform(X)

print("Ursprüngliche X-Shape:", X.shape)
print("X mit ausgewählten Merkmalen Shape:", X_selected.shape)
print("Ausgewählte Merkmale:", sel.get_support(indices=True))
```

Dieser Codeausschnitt demonstriert, wie `VarianceThreshold` verwendet wird, um Null-Varianz-Merkmale aus einem Datensatz zu entfernen. Die Ausgabe zeigt die ursprüngliche Form des Datensatzes und die Form nach der Auswahl von Merkmalen mit hoher Variabilität.
