# Multiclass-Klassifikation

#### Problem-Beschreibung

Multiclass-Klassifikation ist eine Klassifizierungstask mit mehr als zwei Klassen. Jede Probe wird nur einer Klasse zugewiesen.

#### Zielformat

Eine gültige Darstellung von Multiclass-Zielen ist ein eindimensionaler oder Spaltenvektor, der mehr als zwei diskrete Werte enthält.

#### Beispiel

Lassen Sie uns das Iris-Datensatz verwenden, um die Multiclass-Klassifikation zu demonstrieren:

```python
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier

# Lade den Iris-Datensatz
X, y = datasets.load_iris(return_X_y=True)

# Trainiere ein logistisches Regressionsmodell mit OneVsRestClassifier
model = OneVsRestClassifier(LogisticRegression())
model.fit(X, y)

# Mache Vorhersagen
predictions = model.predict(X)
print(predictions)
```
