# Ajuster la régression linéaire non négative

Nous allons maintenant ajuster nos données en utilisant la régression linéaire non négative. Cela se fait en utilisant la classe `LinearRegression` de scikit-learn avec le paramètre `positive=True`. Nous prédirons ensuite les valeurs pour notre ensemble de test et calculerons le score R2.

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

reg_nnls = LinearRegression(positive=True)
y_pred_nnls = reg_nnls.fit(X_train, y_train).predict(X_test)
r2_score_nnls = r2_score(y_test, y_pred_nnls)
print("NNLS R2 score", r2_score_nnls)
```
