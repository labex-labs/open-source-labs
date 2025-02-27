# Multilabel-Klassifikation

#### Problem-Beschreibung

Multilabel-Klassifikation ist eine Klassifizierungstask, bei der jeder Probe mehrere Labels zugewiesen werden können. Die Anzahl der Labels, die jede Probe haben kann, ist größer als zwei.

#### Zielformat

Eine gültige Darstellung von Multilabel-Zielen ist eine binäre Matrix, wobei jede Zeile eine Probe und jede Spalte eine Klasse repräsentiert. Ein Wert von 1 zeigt die Anwesenheit des Labels in der Probe an, während 0 oder -1 die Abwesenheit anzeigt.

#### Beispiel

Lassen Sie uns ein Multilabel-Klassifizierungsproblem mit der make_classification-Funktion erstellen:

```python
from sklearn.datasets import make_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier

# Generiere ein Multilabel-Klassifizierungsproblem
X, y = make_classification(n_samples=100, n_features=10, n_informative=5, random_state=0)
y = y.reshape(-1, 1)

# Trainiere einen Multioutput-Zufälligen-Baum-Klassifizierer
model = MultiOutputClassifier(RandomForestClassifier())
model.fit(X, y)

# Mache Vorhersagen
predictions = model.predict(X)
print(predictions)
```
