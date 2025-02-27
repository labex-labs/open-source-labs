# Вычисление важности признаков перестановки

Теперь мы вычислим важность признаков перестановки с использованием функции `permutation_importance` из scikit - learn. Эта функция принимает на вход обученную модель, валидационный набор данных и количество раз, которое нужно переставлять признаки.

```python
from sklearn.inspection import permutation_importance

# Calculate permutation feature importance
result = permutation_importance(model, X_val, y_val, n_repeats = 30, random_state = 0)

# Print the feature importances
for i in result.importances_mean.argsort()[::-1]:
    if result.importances_mean[i] - 2 * result.importances_std[i] > 0:
        print(f"{диабет.feature_names[i]}: {result.importances_mean[i]:.3f} +/- {result.importances_std[i]:.3f}")
```
