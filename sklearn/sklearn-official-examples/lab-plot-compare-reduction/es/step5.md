# Almacenamiento en caché de transformadores dentro de una tubería

Ahora demostraremos cómo almacenar el estado de un transformador específico, ya que podría ser utilizado nuevamente. Utilizar una tubería en `GridSearchCV` desencadena situaciones como esta. Por lo tanto, usamos el argumento `memory` para habilitar el almacenamiento en caché.

```python
from joblib import Memory
from shutil import rmtree

# Crea una carpeta temporal para almacenar los transformadores de la tubería
ubicación = "cachedir"
memory = Memory(location=ubicación, verbose=10)
cached_pipe = Pipeline(
    [("reduce_dim", PCA()), ("classify", LinearSVC(dual=False, max_iter=10000))],
    memory=memory,
)

# Esta vez, se utilizará una tubería almacenada en caché dentro de la búsqueda en la cuadrícula

# Elimina la caché temporal antes de salir
memory.clear(warn=False)
rmtree(ubicación)
```
