# ElasticNet

ElasticNet is a middle ground between Lasso and Ridge regression, as it combines an L1 and an L2-penalty. The amount of regularization is controlled by the two hyperparameters `l1_ratio` and `alpha`. For `l1_ratio = 0` the penalty is pure L2 and the model is equivalent to a Ridge regression. Similarly, `l1_ratio = 1` is a pure L1 penalty and the model is equivalent to a Lasso regression. For `0 < l1_ratio < 1`, the penalty is a combination of L1 and L2.

```python
from sklearn.linear_model import ElasticNet

t0 = time()
enet = ElasticNet(alpha=0.08, l1_ratio=0.5).fit(X_train, y_train)
print(f"ElasticNet fit done in {(time() - t0):.3f}s")

y_pred_enet = enet.predict(X_test)
r2_score_enet = r2_score(y_test, y_pred_enet)
print(f"ElasticNet r^2 on test data : {r2_score_enet:.3f}")
```


