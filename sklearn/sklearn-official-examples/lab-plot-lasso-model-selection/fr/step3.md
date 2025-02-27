# Sélection de Lasso via un critère d'information

Nous utiliserons la fonction `LassoLarsIC` de `sklearn.linear_model` pour fournir un estimateur Lasso qui utilise le critère d'information d'Akaike (AIC) ou le critère d'information de Bayes (BIC) pour sélectionner la valeur optimale du paramètre de régularisation alpha. Nous allons tout d'abord ajuster un modèle Lasso avec le critère AIC.

```python
import time
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LassoLarsIC
from sklearn.pipeline import make_pipeline

start_time = time.time()
lasso_lars_ic = make_pipeline(StandardScaler(), LassoLarsIC(criterion="aic")).fit(X, y)
fit_time = time.time() - start_time
```
