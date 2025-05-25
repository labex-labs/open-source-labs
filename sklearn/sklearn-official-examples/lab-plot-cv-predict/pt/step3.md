# Gerar Previsões com Validação Cruzada

Usaremos a função `cross_val_predict` do scikit-learn para gerar previsões com validação cruzada.

```python
from sklearn.model_selection import cross_val_predict

y_pred = cross_val_predict(lr, X, y, cv=10)
```
