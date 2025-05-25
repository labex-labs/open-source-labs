# Otimizar Hiperparâmetros

No passo anterior, usamos valores padrão de hiperparâmetros para alpha e gamma. Para melhorar o desempenho do modelo, podemos otimizar esses hiperparâmetros usando busca em grade.

```python
from sklearn.model_selection import GridSearchCV

# Define a grade de parâmetros
param_grid = {'alpha': [1e-3, 1e-2, 1e-1, 1, 10],
              'gamma': [1e-3, 1e-2, 1e-1, 1, 10]}

# Realizar a busca em grade
grid_search = GridSearchCV(krr, param_grid, cv=5)
grid_search.fit(X, y)

# Obter os melhores hiperparâmetros
best_alpha = grid_search.best_params_['alpha']
best_gamma = grid_search.best_params_['gamma']
best_krr = grid_search.best_estimator_

print("Melhor alpha:", best_alpha)
print("Melhor gamma:", best_gamma)
```
