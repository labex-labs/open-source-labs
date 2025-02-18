# Definir el modelo

Utilizamos un clasificador de vectores de soporte con un kernel de función de base radial (radial basis function kernel).

```python
from sklearn.svm import SVC

# We will use a Support Vector Classifier with "rbf" kernel
svm = SVC(kernel="rbf")
```
