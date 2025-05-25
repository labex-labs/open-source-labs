# Ajuste de Hiperparâmetros

Utilizamos RandomizedSearchCV para explorar a grade de hiperparâmetros e encontrar a melhor combinação de hiperparâmetros para o pipeline. Neste caso, definimos `n_iter=40` para limitar o espaço de busca. Podemos aumentar `n_iter` para obter uma análise mais informativa, mas isso aumentará o tempo de computação.

```python
from pprint import pprint
from sklearn.model_selection import RandomizedSearchCV

random_search = RandomizedSearchCV(
    estimator=pipeline,
    param_distributions=parameter_grid,
    n_iter=40,
    random_state=0,
    n_jobs=2,
    verbose=1,
)

print("Executando busca em grade...")
print("Hiperparâmetros a serem avaliados:")
pprint(parameter_grid)

random_search.fit(data_train.data, data_train.target)

test_accuracy = random_search.score(data_test.data, data_test.target)
```
