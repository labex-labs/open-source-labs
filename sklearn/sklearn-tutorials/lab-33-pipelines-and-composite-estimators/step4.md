# TransformedTargetRegressor

The `TransformedTargetRegressor` class is used to transform the target variable in a regression problem before fitting a regression model. This is useful when you want to apply a transformation to the target variable, such as taking the logarithm. The predictions are mapped back to the original space via an inverse transform. Here is an example of using `TransformedTargetRegressor` with a linear regression model and a quantile transformer:

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
