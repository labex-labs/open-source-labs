# Lasso

Nesta etapa, demonstraremos como utilizar o modelo de regressão Lasso para estimar os coeficientes esparsos do conjunto de dados. Usaremos um valor fixo do parâmetro de regularização `alpha`. Na prática, o parâmetro ótimo `alpha` deve ser selecionado passando uma estratégia de validação cruzada `TimeSeriesSplit` para um `LassoCV`. Para manter o exemplo simples e rápido de executar, definimos diretamente o valor ótimo para alpha aqui.

```python
from sklearn.linear_model import Lasso
from sklearn.metrics import r2_score
from time import time

t0 = time()
lasso = Lasso(alpha=0.14).fit(X_train, y_train)
print(f"Lasso fit done in {(time() - t0):.3f}s")

y_pred_lasso = lasso.predict(X_test)
r2_score_lasso = r2_score(y_test, y_pred_lasso)
print(f"Lasso r^2 on test data : {r2_score_lasso:.3f}")
```
