# Feature Importance from Coefficients

To get an idea of the importance of the features, we use the RidgeCV estimator. The features with the highest absolute `coef_` value are considered the most important.

```python
from sklearn.linear_model import RidgeCV

ridge = RidgeCV(alphas=np.logspace(-6, 6, num=5)).fit(X, y)
importance = np.abs(ridge.coef_)
feature_names = np.array(diabetes.feature_names)
plt.bar(height=importance, x=feature_names)
plt.title("Feature importances via coefficients")
plt.show()
```


