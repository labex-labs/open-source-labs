# Multiclass-Multioutput-Klassifikation

#### Problem-Beschreibung

Multiclass-Multioutput-Klassifikation, auch als Multitask-Klassifikation bekannt, prognostiziert mehrere nicht-binäre Eigenschaften für jede Probe. Jede Eigenschaft kann mehr als zwei Klassen haben.

#### Zielformat

Eine gültige Darstellung von Multiclass-Multioutput-Zielen ist eine dichte Matrix, wobei jede Zeile eine Probe und jede Spalte eine unterschiedliche Eigenschaft oder Klasse repräsentiert.

#### Beispiel

Lassen Sie uns ein Multiclass-Multioutput-Klassifizierungsproblem mit der make_classification-Funktion erstellen:

```python
from sklearn.datasets import make_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.svm import SVC

# Generiere ein Multiclass-Multioutput-Klassifizierungsproblem
X, y = make_classification(n_samples=100, n_features=10, n_informative=5, n_classes=3, random_state=0)

# Trainiere einen Multioutput-Support-Vector-Klassifizierer
model = MultiOutputClassifier(SVC())
model.fit(X, y)

# Mache Vorhersagen
predictions = model.predict(X)
print(predictions)
```
