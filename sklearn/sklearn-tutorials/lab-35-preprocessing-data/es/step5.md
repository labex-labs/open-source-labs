# Imputación de Valores Faltantes

Los valores faltantes en un conjunto de datos pueden causar problemas con los algoritmos de aprendizaje automático. Podemos utilizar los métodos proporcionados en el módulo `impute` de scikit-learn para manejar los valores faltantes. Aquí, usaremos el `SimpleImputer` para imputar valores faltantes.

```python
from sklearn.impute import SimpleImputer
import numpy as np

# Crea un conjunto de datos de muestra con valores faltantes
X = np.array([[1., 2., np.nan],
              [3., np.nan, 5.],
              [np.nan, 4., 6.]])

# Inicializa el SimpleImputer
imputer = SimpleImputer()

# Ajusta y transforma los datos de entrenamiento
X_imputed = imputer.fit_transform(X)

# Imprime los datos transformados
print(X_imputed)
```
