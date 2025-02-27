# Escalado

Escalar las características a un rango específico es otra técnica de preprocesamiento común. Es útil cuando las características tienen diferentes escalas y queremos que todas estén en un rango similar. El `MinMaxScaler` y el `MaxAbsScaler` se pueden utilizar para realizar el escalado.

```python
from sklearn.preprocessing import MinMaxScaler, MaxAbsScaler
import numpy as np

# Crea un conjunto de datos de muestra
X = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])

# Inicializa el MinMaxScaler
min_max_scaler = MinMaxScaler()

# Ajusta y transforma los datos de entrenamiento
X_minmax = min_max_scaler.fit_transform(X)

# Imprime los datos transformados
print(X_minmax)

# Inicializa el MaxAbsScaler
max_abs_scaler = MaxAbsScaler()

# Ajusta y transforma los datos de entrenamiento
X_maxabs = max_abs_scaler.fit_transform(X)

# Imprime los datos transformados
print(X_maxabs)
```
