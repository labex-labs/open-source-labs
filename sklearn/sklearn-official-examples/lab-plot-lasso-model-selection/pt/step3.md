# Selecionando Lasso via um Critério de Informação

Usaremos a função `LassoLarsIC` de `sklearn.linear_model` para fornecer um estimador Lasso que utiliza o critério de informação de Akaike (AIC) ou o critério de informação de Bayes (BIC) para selecionar o valor ótimo do parâmetro de regularização alfa. Primeiro, ajustaremos um modelo Lasso com o critério AIC.

```python
import time
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LassoLarsIC
from sklearn.pipeline import make_pipeline

start_time = time.time()
lasso_lars_ic = make_pipeline(StandardScaler(), LassoLarsIC(criterion="aic")).fit(X, y)
fit_time = time.time() - start_time
```
