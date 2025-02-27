# Cargar datos y entrenar un SVC

Comenzaremos cargando el conjunto de datos de vinos y convirtiéndolo en un problema de clasificación binaria. Luego, entrenaremos un clasificador de vectores de soporte en el conjunto de datos de entrenamiento.

```python
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import RocCurveDisplay
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

X, y = load_wine(return_X_y=True)
y = y == 2

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
svc = SVC(random_state=42)
svc.fit(X_train, y_train)
```
