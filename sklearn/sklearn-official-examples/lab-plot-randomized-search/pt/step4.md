# Busca em grade para otimização de hiperparâmetros

Usaremos busca em grade para explorar o espaço de hiperparâmetros e encontrar os melhores hiperparâmetros para nosso modelo SVM.

```python
# especifique os parâmetros a serem pesquisados
param_grid = {
    "average": [True, False],
    "l1_ratio": np.linspace(0, 1, num=10),
    "alpha": np.power(10, np.arange(-2, 1, dtype=float)),
}

# execute a busca em grade
grid_search = GridSearchCV(clf, param_grid=param_grid)

start = time()
grid_search.fit(X, y)

print(
    "GridSearchCV levou %.2f segundos para %d configurações de parâmetros candidatas."
    % (time() - start, len(grid_search.cv_results_["params"]))
)

# imprime os resultados
report(grid_search.cv_results_)
```
