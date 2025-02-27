# Lasso

Dans cette étape, nous allons démontrer comment utiliser le modèle de régression Lasso pour estimer les coefficients creux de l'ensemble de données. Nous utiliserons une valeur fixe du paramètre de régularisation `alpha`. En pratique, le paramètre optimal `alpha` devrait être sélectionné en passant une stratégie de validation croisée `TimeSeriesSplit` à un `LassoCV`. Pour garder l'exemple simple et rapide à exécuter, nous définissons directement la valeur optimale pour alpha ici.

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
