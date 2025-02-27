# TransformedTargetRegressor

La clase `TransformedTargetRegressor` se utiliza para transformar la variable objetivo en un problema de regresión antes de ajustar un modelo de regresión. Esto es útil cuando desea aplicar una transformación a la variable objetivo, como tomar el logaritmo. Las predicciones se mapean de vuelta al espacio original a través de una transformación inversa. Aquí hay un ejemplo de uso de `TransformedTargetRegressor` con un modelo de regresión lineal y un transformador cuantil:

```python
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.compose import TransformedTargetRegressor
from sklearn.preprocessing import QuantileTransformer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X, y = fetch_california_housing(return_X_y=True)
transformer = QuantileTransformer(output_distribution='normal')
regressor = LinearRegression()
regr = TransformedTargetRegressor(regressor=regressor, transformer=transformer)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
regr.fit(X_train, y_train)
regr.score(X_test, y_test)
```
