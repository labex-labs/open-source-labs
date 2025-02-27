# Erstelle das RFE-Objekt und passe die Daten an

Als nächstes werden wir ein Objekt der RFE-Klasse erstellen und die Daten darauf anpassen. Wir werden einen Support Vector Classifier (SVC) mit einem linearen Kernel als Schätzer verwenden. Wir werden jeweils einen Feature auswählen und Schritt für Schritt vorgehen.

```python
from sklearn.svm import SVC
from sklearn.feature_selection import RFE

svc = SVC(kernel="linear", C=1)
rfe = RFE(estimator=svc, n_features_to_select=1, step=1)
rfe.fit(X, y)
```
