# Passt das SVM-Modell an

Als nächstes werden wir das SVM-Modell an unseren Datensatz anpassen, indem wir einen linearen Kernel und einen Regularisierungsparameter von 1000 verwenden. Wir werden die Funktion `svm.SVC()` aus scikit-learn verwenden, um den SVM-Classifier zu erstellen.

```python
from sklearn import svm

# fit the SVM model
clf = svm.SVC(kernel="linear", C=1000)
clf.fit(X, y)
```
