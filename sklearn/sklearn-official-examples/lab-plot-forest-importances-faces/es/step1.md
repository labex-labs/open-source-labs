# Cargar los datos y ajuste del modelo

Comenzamos cargando el conjunto de datos Olivetti Faces y limitando el conjunto de datos para que solo contenga las primeras cinco clases. Luego entrenamos un bosque aleatorio en el conjunto de datos y evaluamos la importancia de las características basada en la impureza. Estableceremos el número de núcleos que se usarán para las tareas.

```python
from sklearn.datasets import fetch_olivetti_faces

# Seleccionamos el número de núcleos que se usarán para realizar el ajuste en paralelo
# del modelo del bosque. `-1` significa usar todos los núcleos disponibles.
n_jobs = -1

# Cargar el conjunto de datos de caras
data = fetch_olivetti_faces()
X, y = data.data, data.target

# Limitar el conjunto de datos a 5 clases.
mask = y < 5
X = X[mask]
y = y[mask]

# Se ajustará un clasificador de bosque aleatorio para calcular las importancias de las características.
from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier(n_estimators=750, n_jobs=n_jobs, random_state=42)

forest.fit(X, y)
```
