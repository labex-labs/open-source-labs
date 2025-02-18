# Definition des Modells

Wir verwenden einen Support-Vektor-Klassifikator (Support vector classifier) mit einem Radialbasisfunktions-Kernel (radial basis function kernel).

```python
from sklearn.svm import SVC

# We will use a Support Vector Classifier with "rbf" kernel
svm = SVC(kernel="rbf")
```
