# Definir el estimador y la cuadrícula de parámetros

Ahora necesitamos definir el estimador que queremos ajustar y la cuadrícula de parámetros que queremos buscar. La cuadrícula de parámetros especifica los valores que queremos probar para cada hiperparámetro.

```python
from sklearn.svm import SVC

# Crear una instancia del clasificador de vectores de soporte
svc = SVC()

# Definir la cuadrícula de parámetros
param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [0.1, 0.01, 0.001], 'kernel': ['linear', 'rbf']}
```
