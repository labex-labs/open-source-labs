# Einvariate Feature-Selektion

Die einvariable Feature-Selektion funktioniert, indem die besten Merkmale auf der Grundlage einvarianter statistischer Tests ausgewählt werden. In scikit-learn gibt es mehrere Klassen, die die einvariable Feature-Selektion implementieren:

- `SelectKBest`: Wählt die k besten Merkmale mit den höchsten Bewertungen aus
- `SelectPercentile`: Wählt einen benutzerdefinierten Prozentsatz der Merkmale mit den höchsten Bewertungen aus
- `SelectFpr`: Wählt Merkmale auf der Grundlage der falschen Positivrate
- `SelectFdr`: Wählt Merkmale auf der Grundlage der falschen Entdeckungsrate
- `SelectFwe`: Wählt Merkmale auf der Grundlage des familiären Fehlers
- `GenericUnivariateSelect`: Ermöglicht die Auswahl mit einer konfigurierbaren Strategie

Hier ist ein Beispiel für die Verwendung von `SelectKBest`, um die zwei besten Merkmale aus dem Iris-Datensatz auszuwählen:

```python
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

# Lade den Iris-Datensatz
X, y = load_iris(return_X_y=True)

# Initialisiere SelectKBest mit der Bewertungsfunktion f_classif und k=2
selector = SelectKBest(f_classif, k=2)

# Wähle die besten Merkmale
X_selected = selector.fit_transform(X, y)

print("Ursprüngliche X-Shape:", X.shape)
print("X mit ausgewählten Merkmalen Shape:", X_selected.shape)
print("Ausgewählte Merkmale:", selector.get_support(indices=True))
```

In diesem Beispiel verwenden wir die Bewertungsfunktion `f_classif` und wählen die zwei besten Merkmale aus dem Iris-Datensatz aus. Die Ausgabe zeigt die ursprüngliche Form des Datensatzes und die Form nach der Auswahl der besten Merkmale.
