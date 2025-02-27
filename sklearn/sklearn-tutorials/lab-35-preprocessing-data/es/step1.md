# Estandarización

La estandarización es un paso de preprocesamiento común para muchos algoritmos de aprendizaje automático. Transforma las características para que tengan media cero y varianza unitaria. Podemos utilizar el `StandardScaler` de scikit-learn para realizar la estandarización.

```python
from sklearn.preprocessing import StandardScaler
import numpy as np

# Crea un conjunto de datos de muestra
X = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])

# Inicializa el StandardScaler
scaler = StandardScaler()

# Ajusta el escalador a los datos de entrenamiento
scaler.fit(X)

# Transforma los datos de entrenamiento
X_scaled = scaler.transform(X)

# Imprime los datos transformados
print(X_scaled)
```
