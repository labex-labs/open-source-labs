# Configurar los clasificadores de Label Spreading

Configuraremos tres clasificadores de Label Spreading con diferentes porcentajes de datos etiquetados: 30%, 50% y 100%. Label Spreading es un algoritmo de aprendizaje semi-supervisado que propaga las etiquetas de los puntos de datos etiquetados a los no etiquetados basado en la similitud entre ellos.

```python
from sklearn.semi_supervised import LabelSpreading

# Configurar los clasificadores de Label Spreading
rng = np.random.RandomState(0)
y_rand = rng.rand(y.shape[0])
y_30 = np.copy(y)
y_30[y_rand < 0.3] = -1  # establecer muestras aleatorias como no etiquetadas
y_50 = np.copy(y)
y_50[y_rand < 0.5] = -1
ls30 = (LabelSpreading().fit(X, y_30), y_30, "Label Spreading 30% data")
ls50 = (LabelSpreading().fit(X, y_50), y_50, "Label Spreading 50% data")
ls100 = (LabelSpreading().fit(X, y), y, "Label Spreading 100% data")
```
