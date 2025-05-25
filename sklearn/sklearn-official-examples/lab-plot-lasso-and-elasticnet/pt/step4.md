# ElasticNet

ElasticNet é um ponto intermediário entre a regressão Lasso e Ridge, pois combina uma penalidade L1 e uma penalidade L2. A quantidade de regularização é controlada pelos dois hiperparâmetros `l1_ratio` e `alpha`. Para `l1_ratio = 0`, a penalidade é puramente L2 e o modelo é equivalente a uma regressão Ridge. Analogamente, `l1_ratio = 1` é uma penalidade puramente L1 e o modelo é equivalente a uma regressão Lasso. Para `0 < l1_ratio < 1`, a penalidade é uma combinação de L1 e L2.

```python
from sklearn.linear_model import ElasticNet

t0 = time()
enet = ElasticNet(alpha=0.08, l1_ratio=0.5).fit(X_train, y_train)
print(f"ElasticNet fit done in {(time() - t0):.3f}s")

y_pred_enet = enet.predict(X_test)
r2_score_enet = r2_score(y_test, y_pred_enet)
print(f"ElasticNet r^2 on test data : {r2_score_enet:.3f}")
```
