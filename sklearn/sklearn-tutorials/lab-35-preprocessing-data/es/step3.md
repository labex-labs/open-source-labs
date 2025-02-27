# Normalización

La normalización es el proceso de escalar las muestras individuales para que tengan norma unitaria. Se utiliza comúnmente cuando la magnitud de los datos no es importante y solo nos interesa la dirección (o el ángulo) de los datos. Podemos utilizar el `Normalizer` de scikit-learn para realizar la normalización.

```python
from sklearn.preprocessing import Normalizer
import numpy as np

# Crea un conjunto de datos de muestra
X = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])

# Inicializa el Normalizer
normalizer = Normalizer()

# Ajusta y transforma los datos de entrenamiento
X_normalized = normalizer.fit_transform(X)

# Imprime los datos transformados
print(X_normalized)
```
