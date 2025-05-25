# TransformedTargetRegressor

A classe `TransformedTargetRegressor` é usada para transformar a variável alvo num problema de regressão antes de ajustar um modelo de regressão. Isto é útil quando se pretende aplicar uma transformação à variável alvo, como tomar o logaritmo. As previsões são mapeadas de volta ao espaço original através de uma transformação inversa. Aqui está um exemplo de utilização de `TransformedTargetRegressor` com um modelo de regressão linear e um transformador de quantis:

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
