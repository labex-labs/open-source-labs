# Определение модели

Мы используем классификатор на основе опорных векторов (Support Vector Classifier) с ядром радиальной базисной функции (radial basis function kernel).

```python
from sklearn.svm import SVC

# We will use a Support Vector Classifier with "rbf" kernel
svm = SVC(kernel="rbf")
```
