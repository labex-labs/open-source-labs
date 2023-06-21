# Generate Cross-Validated Predictions

We will use `cross_val_predict` function from scikit-learn to generate cross-validated predictions.

```python
from sklearn.model_selection import cross_val_predict

y_pred = cross_val_predict(lr, X, y, cv=10)
```
