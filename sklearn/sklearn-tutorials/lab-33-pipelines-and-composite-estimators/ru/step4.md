# TransformedTargetRegressor

Класс `TransformedTargetRegressor` используется для преобразования целевой переменной в задаче регрессии перед подгонкой модели регрессии. Это полезно, когда вы хотите применить преобразование к целевой переменной, например, взять логарифм. Предсказания отображаются обратно в исходное пространство с помощью обратного преобразования. Вот пример использования `TransformedTargetRegressor` с моделью линейной регрессии и трансформером квантилей:

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
