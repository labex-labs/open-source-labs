# TransformedTargetRegressor

La classe `TransformedTargetRegressor` est utilisée pour transformer la variable cible dans un problème de régression avant d'ajuster un modèle de régression. Cela est utile lorsque vous voulez appliquer une transformation à la variable cible, telle que prendre le logarithme. Les prédictions sont ramenées à l'espace d'origine via une transformation inverse. Voici un exemple d'utilisation de `TransformedTargetRegressor` avec un modèle de régression linéaire et un transformateur quantile :

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
