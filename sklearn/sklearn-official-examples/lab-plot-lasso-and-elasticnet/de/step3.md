# Automatic Relevance Determination (ARD)

Eine ARD-Regression ist die bayesische Version des Lasso. Sie kann, wenn erforderlich, Intervallschätzungen für alle Parameter, einschließlich der Fehlervarianz, liefern. Es ist eine geeignete Option, wenn die Signale Gaussian-Rauschen aufweisen.

```python
from sklearn.linear_model import ARDRegression

t0 = time()
ard = ARDRegression().fit(X_train, y_train)
print(f"ARD fit done in {(time() - t0):.3f}s")

y_pred_ard = ard.predict(X_test)
r2_score_ard = r2_score(y_test, y_pred_ard)
print(f"ARD r^2 on test data : {r2_score_ard:.3f}")
```
