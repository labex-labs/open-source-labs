# Importancia de las características a partir de los coeficientes

Para obtener una idea de la importancia de las características, utilizamos el estimador RidgeCV. Las características con el valor absoluto más alto de `coef_` se consideran las más importantes.

```python
from sklearn.linear_model import RidgeCV

ridge = RidgeCV(alphas=np.logspace(-6, 6, num=5)).fit(X, y)
importance = np.abs(ridge.coef_)
feature_names = np.array(diabetes.feature_names)
plt.bar(height=importance, x=feature_names)
plt.title("Feature importances via coefficients")
plt.show()
```
