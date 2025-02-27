# Generar predicciones validadas cruzadamente

Usaremos la función `cross_val_predict` de scikit-learn para generar predicciones validadas cruzadamente.

```python
from sklearn.model_selection import cross_val_predict

y_pred = cross_val_predict(lr, X, y, cv=10)
```
