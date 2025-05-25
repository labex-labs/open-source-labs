# Calcular a importância da permutação das características

Agora, calcularemos a importância da permutação das características usando a função `permutation_importance` do scikit-learn. Esta função recebe como entrada o modelo treinado, o conjunto de validação e o número de vezes que as características devem ser permutadas.

```python
from sklearn.inspection import permutation_importance

# Calcular a importância da permutação das características
result = permutation_importance(model, X_val, y_val, n_repeats=30, random_state=0)

# Imprimir as importâncias das características
for i in result.importances_mean.argsort()[::-1]:
    if result.importances_mean[i] - 2 * result.importances_std[i] > 0:
        print(f"{diabetes.feature_names[i]}: {result.importances_mean[i]:.3f} +/- {result.importances_std[i]:.3f}")
```
