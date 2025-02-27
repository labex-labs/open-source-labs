# Ajuste de hiperparámetros

Usamos RandomizedSearchCV para explorar la cuadrícula de hiperparámetros y encontrar la mejor combinación de hiperparámetros para la canalización. En este caso, establecemos n_iter = 40 para limitar el espacio de búsqueda. Podemos aumentar n_iter para obtener un análisis más informativo, pero aumentará el tiempo de cálculo.

```python
from sklearn.model_selection import RandomizedSearchCV

random_search = RandomizedSearchCV(
    estimator=pipeline,
    param_distributions=parameter_grid,
    n_iter=40,
    random_state=0,
    n_jobs=2,
    verbose=1,
)

print("Realizando búsqueda en cuadrícula...")
print("Hiperparámetros a evaluar:")
pprint(parameter_grid)

random_search.fit(data_train.data, data_train.target)

test_accuracy = random_search.score(data_test.data, data_test.target)

```
