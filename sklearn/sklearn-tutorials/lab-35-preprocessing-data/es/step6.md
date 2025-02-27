# Generación de Características Polinómicas

A veces es beneficioso agregar complejidad a un modelo considerando las características no lineales de los datos de entrada. Podemos utilizar `PolynomialFeatures` de scikit-learn para generar características polinómicas.

```python
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Crea un conjunto de datos de muestra
X = np.array([[0, 1],
              [2, 3],
              [4, 5]])

# Inicializa PolynomialFeatures
poly = PolynomialFeatures(2)

# Ajusta y transforma los datos de entrenamiento
X_poly = poly.fit_transform(X)

# Imprime los datos transformados
print(X_poly)
```
