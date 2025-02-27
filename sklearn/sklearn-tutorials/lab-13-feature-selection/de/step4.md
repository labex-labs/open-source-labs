# Feature-Selektion mit SelectFromModel

Die Klasse `SelectFromModel` ist ein Meta-Transformer, der mit jedem Schätzer verwendet werden kann, der jeder Eigenschaft eine Wichtigkeit zuweist. Es wählt Merkmale aufgrund ihrer Wichtigkeit aus und entfernt Merkmale, die unter einem bestimmten Schwellenwert liegen.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectFromModel

# Lade den Iris-Datensatz
X, y = load_iris(return_X_y=True)

# Initialisiere RandomForestClassifier als Schätzer
estimator = RandomForestClassifier()

# Initialisiere SelectFromModel mit dem Schätzer und dem Schwellenwert "mean"
selector = SelectFromModel(estimator, threshold="mean")

# Wähle die besten Merkmale
X_selected = selector.fit_transform(X, y)

print("Ursprüngliche X-Shape:", X.shape)
print("X mit ausgewählten Merkmalen Shape:", X_selected.shape)
print("Ausgewählte Merkmale:", selector.get_support(indices=True))
```

In diesem Beispiel verwenden wir einen Random Forest Classifier als Schätzer und wählen Merkmale aus, deren Wichtigkeit größer als die durchschnittliche Wichtigkeit ist. Die Ausgabe zeigt die ursprüngliche Form des Datensatzes und die Form nach der Auswahl der besten Merkmale.
