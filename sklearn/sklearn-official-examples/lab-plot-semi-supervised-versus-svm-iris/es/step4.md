# Configurar el clasificador de SVM

Configuraremos un clasificador de SVM con un kernel de función radial de base (RBF). El SVM es un algoritmo de aprendizaje supervisado que encuentra el hiperplano óptimo que separa los datos en diferentes clases.

```python
from sklearn.svm import SVC

# Configurar el clasificador de SVM
rbf_svc = (SVC(kernel="rbf", gamma=0.5).fit(X, y), y, "SVC with rbf kernel")
```
