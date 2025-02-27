# Automatic Relevance Determination (ARD)

Une régression ARD est la version bayésienne du Lasso. Elle peut produire des estimations d'intervalle pour tous les paramètres, y compris la variance d'erreur, si nécessaire. C'est une option appropriée lorsque les signaux ont un bruit gaussien.

```python
from sklearn.linear_model import ARDRegression

t0 = time()
ard = ARDRegression().fit(X_train, y_train)
print(f"ARD fit done in {(time() - t0):.3f}s")

y_pred_ard = ard.predict(X_test)
r2_score_ard = r2_score(y_test, y_pred_ard)
print(f"ARD r^2 on test data : {r2_score_ard:.3f}")
```
