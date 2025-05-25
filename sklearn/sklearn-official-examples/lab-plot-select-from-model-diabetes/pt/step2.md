# Importância das Características a Partir dos Coeficientes

Para obter uma ideia da importância das características, utilizamos o estimador RidgeCV. As características com o valor absoluto de `coef_` mais elevado são consideradas as mais importantes.

```python
from sklearn.linear_model import RidgeCV

ridge = RidgeCV(alphas=np.logspace(-6, 6, num=5)).fit(X, y)
importance = np.abs(ridge.coef_)
feature_names = np.array(diabetes.feature_names)
plt.bar(height=importance, x=feature_names)
plt.title("Importâncias das características através dos coeficientes")
plt.show()
```
