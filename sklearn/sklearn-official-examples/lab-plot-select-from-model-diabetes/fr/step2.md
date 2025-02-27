# Importance des fonctionnalités à partir des coefficients

Pour avoir une idée de l'importance des fonctionnalités, nous utilisons l'estimateur RidgeCV. Les fonctionnalités ayant la valeur absolue la plus élevée de `coef_` sont considérées comme les plus importantes.

```python
from sklearn.linear_model import RidgeCV

ridge = RidgeCV(alphas=np.logspace(-6, 6, num=5)).fit(X, y)
importance = np.abs(ridge.coef_)
feature_names = np.array(diabetes.feature_names)
plt.bar(height=importance, x=feature_names)
plt.title("Feature importances via coefficients")
plt.show()
```
