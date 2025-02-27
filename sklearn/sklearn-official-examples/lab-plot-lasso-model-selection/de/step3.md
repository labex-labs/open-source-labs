# Auswahl von Lasso über ein Informationskriterium

Wir werden die Funktion `LassoLarsIC` aus `sklearn.linear_model` verwenden, um einen Lasso-Schätzer bereitzustellen, der das Akaike-Informationskriterium (AIC) oder das Bayes-Informationskriterium (BIC) verwendet, um den optimalen Wert des Regularisierungsparameters Alpha zu wählen. Wir werden zunächst ein Lasso-Modell mit dem AIC-Kriterium anpassen.

```python
import time
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LassoLarsIC
from sklearn.pipeline import make_pipeline

start_time = time.time()
lasso_lars_ic = make_pipeline(StandardScaler(), LassoLarsIC(criterion="aic")).fit(X, y)
fit_time = time.time() - start_time
```
