# Ajustar Regressão de Mínimos Quadrados Não Negativos

Agora, ajustaremos os nossos dados usando regressão de mínimos quadrados não negativos. Isto é feito usando a classe `LinearRegression` do scikit-learn com o parâmetro `positive=True`. Em seguida, preveremos os valores para o nosso conjunto de teste e calcularemos a pontuação R2.

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

reg_nnls = LinearRegression(positive=True)
y_pred_nnls = reg_nnls.fit(X_train, y_train).predict(X_test)
r2_score_nnls = r2_score(y_test, y_pred_nnls)
print("NNLS R2 score", r2_score_nnls)
```
