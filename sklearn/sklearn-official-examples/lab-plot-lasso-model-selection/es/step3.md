# Seleccionando Lasso a través de un criterio de información

Usaremos la función `LassoLarsIC` de `sklearn.linear_model` para proporcionar un estimador de Lasso que utiliza el criterio de información de Akaike (AIC) o el criterio de información bayesiano (BIC) para seleccionar el valor óptimo del parámetro de regularización alfa. Primero ajustaremos un modelo Lasso con el criterio AIC.

```python
import time
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LassoLarsIC
from sklearn.pipeline import make_pipeline

start_time = time.time()
lasso_lars_ic = make_pipeline(StandardScaler(), LassoLarsIC(criterion="aic")).fit(X, y)
fit_time = time.time() - start_time
```
