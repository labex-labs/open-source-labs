# Regresión multi-salida

#### Descripción del problema

La regresión multi-salida predice múltiples propiedades numéricas para cada muestra. Cada propiedad es una variable numérica y el número de propiedades puede ser mayor o igual a dos.

#### Formato de destino

Una representación válida de objetivos de regresión multi-salida es una matriz densa, donde cada fila representa una muestra y cada columna representa una propiedad diferente.

#### Ejemplo

Vamos a crear un problema de regresión multi-salida usando la función make_regression:

```python
from sklearn.datasets import make_regression
from sklearn.multioutput import MultiOutputRegressor
from sklearn.linear_model import LinearRegression

# Generar un problema de regresión multi-salida
X, y = make_regression(n_samples=100, n_features=10, n_targets=3, random_state=0)

# Ajustar un modelo de regresión lineal multi-salida
model = MultiOutputRegressor(LinearRegression())
model.fit(X, y)

# Hacer predicciones
predictions = model.predict(X)
print(predictions)
```
