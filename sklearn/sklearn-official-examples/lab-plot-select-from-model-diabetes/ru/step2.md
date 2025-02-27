# Важность признаков по коэффициентам

Для оценки важности признаков мы используем оценщик RidgeCV. Признаки с наибольшим абсолютным значением `coef_` считаются самыми важными.

```python
from sklearn.linear_model import RidgeCV

ridge = RidgeCV(alphas=np.logspace(-6, 6, num=5)).fit(X, y)
importance = np.abs(ridge.coef_)
feature_names = np.array(diabetes.feature_names)
plt.bar(height=importance, x=feature_names)
plt.title("Feature importances via coefficients")
plt.show()
```
