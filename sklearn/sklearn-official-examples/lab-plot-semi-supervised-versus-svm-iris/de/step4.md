# Einrichten des SVM-Klassifizierers

Wir werden einen SVM-Klassifizierer mit einem radial basis function (RBF)-Kernel einrichten. SVM ist ein überwachtes Lernverfahren, das die optimale Hyperebene sucht, die die Daten in verschiedene Klassen trennt.

```python
from sklearn.svm import SVC

# Einrichten des SVM-Klassifizierers
rbf_svc = (SVC(kernel="rbf", gamma=0.5).fit(X, y), y, "SVC mit rbf-Kernel")
```
