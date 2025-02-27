# ElasticNet

ElasticNet ist ein Mittelweg zwischen Lasso- und Ridge-Regression, da es eine L1- und eine L2-Strafe kombiniert. Die Stärke der Regularisierung wird durch die beiden Hyperparameter `l1_ratio` und `alpha` kontrolliert. Für `l1_ratio = 0` ist die Strafe reine L2 und das Modell entspricht einer Ridge-Regression. Ähnlich ist `l1_ratio = 1` eine reine L1-Strafe und das Modell entspricht einer Lasso-Regression. Für `0 < l1_ratio < 1` ist die Strafe eine Kombination aus L1 und L2.

```python
from sklearn.linear_model import ElasticNet

t0 = time()
enet = ElasticNet(alpha=0.08, l1_ratio=0.5).fit(X_train, y_train)
print(f"ElasticNet fit done in {(time() - t0):.3f}s")

y_pred_enet = enet.predict(X_test)
r2_score_enet = r2_score(y_test, y_pred_enet)
print(f"ElasticNet r^2 on test data : {r2_score_enet:.3f}")
```
