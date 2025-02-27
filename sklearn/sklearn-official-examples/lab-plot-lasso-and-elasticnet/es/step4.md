# ElasticNet

ElasticNet es un enfoque intermedio entre la regresión Lasso y Ridge, ya que combina una penalización L1 y una penalización L2. La cantidad de regularización está controlada por los dos hiperparámetros `l1_ratio` y `alpha`. Para `l1_ratio = 0`, la penalización es pura L2 y el modelo es equivalente a una regresión Ridge. Del mismo modo, `l1_ratio = 1` es una penalización pura L1 y el modelo es equivalente a una regresión Lasso. Para `0 < l1_ratio < 1`, la penalización es una combinación de L1 y L2.

```python
from sklearn.linear_model import ElasticNet

t0 = time()
enet = ElasticNet(alpha=0.08, l1_ratio=0.5).fit(X_train, y_train)
print(f"ElasticNet fit done in {(time() - t0):.3f}s")

y_pred_enet = enet.predict(X_test)
r2_score_enet = r2_score(y_test, y_pred_enet)
print(f"ElasticNet r^2 on test data : {r2_score_enet:.3f}")
```
