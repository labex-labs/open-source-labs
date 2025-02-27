# Rekursive Feature-Eliminierung

Die rekursive Feature-Eliminierung (RFE) ist eine Feature-Selektionsmethode, die rekursiv immer kleinere Mengen von Merkmalen betrachtet, um die wichtigsten zu wählen. Sie funktioniert, indem ein externer Schätzer mit Gewichten für die Merkmale trainiert und die am wenigsten wichtigen Merkmale abgeschnitten werden.

```python
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.feature_selection import RFE

# Lade den Iris-Datensatz
X, y = load_iris(return_X_y=True)

# Initialisiere SVC als externen Schätzer
estimator = SVC(kernel="linear")

# Initialisiere RFE mit dem externen Schätzer und wähle 2 Merkmale
selector = RFE(estimator, n_features_to_select=2)

# Wähle die besten Merkmale
X_selected = selector.fit_transform(X, y)

print("Ursprüngliche X-Shape:", X.shape)
print("X mit ausgewählten Merkmalen Shape:", X_selected.shape)
print("Ausgewählte Merkmale:", selector.get_support(indices=True))
```

In diesem Beispiel verwenden wir einen Support Vector Classifier (SVC) als externen Schätzer und wählen die zwei besten Merkmale aus dem Iris-Datensatz aus. Die Ausgabe zeigt die ursprüngliche Form des Datensatzes und die Form nach der Auswahl der besten Merkmale.
