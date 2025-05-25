# Treinar o modelo

Em seguida, treinaremos um modelo de regressão nos dados de treinamento. Neste exemplo, usaremos um modelo de regressão Ridge.

```python
from sklearn.linear_model import Ridge

# Treinar o modelo de regressão Ridge
model = Ridge(alpha=1e-2).fit(X_train, y_train)
```
