# TransformedTargetRegressor

Die `TransformedTargetRegressor`-Klasse wird verwendet, um die Zielvariable in einem Regressionsproblem vor dem Anpassen eines Regressionsmodells zu transformieren. Dies ist nützlich, wenn Sie eine Transformation auf die Zielvariable anwenden möchten, wie z. B. das Nehmen des Logarithmus. Die Vorhersagen werden über eine inverse Transformation zurück in den ursprünglichen Raum abgebildet. Hier ist ein Beispiel für die Verwendung von `TransformedTargetRegressor` mit einem linearen Regressionsmodell und einem Quantile-Transformer:

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
