# Calcular la importancia de las características por permutación

Ahora, calcularemos la importancia de las características por permutación utilizando la función `permutation_importance` de scikit-learn. Esta función toma como entrada el modelo entrenado, el conjunto de validación y el número de veces que se deben permutar las características.

```python
from sklearn.inspection import permutation_importance

# Calcular la importancia de las características por permutación
result = permutation_importance(model, X_val, y_val, n_repeats=30, random_state=0)

# Imprimir las importancias de las características
for i in result.importances_mean.argsort()[::-1]:
    if result.importances_mean[i] - 2 * result.importances_std[i] > 0:
        print(f"{diabetes.feature_names[i]}: {result.importances_mean[i]:.3f} +/- {result.importances_std[i]:.3f}")
```
