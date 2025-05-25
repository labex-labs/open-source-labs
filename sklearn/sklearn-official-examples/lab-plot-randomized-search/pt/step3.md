# Busca aleatória para otimização de hiperparâmetros

Usaremos busca aleatória para explorar o espaço de hiperparâmetros e encontrar os melhores hiperparâmetros para nosso modelo SVM.

```python
# especifique os parâmetros e as distribuições para amostragem
param_dist = {
    "average": [True, False],
    "l1_ratio": stats.uniform(0, 1),
    "alpha": stats.loguniform(1e-2, 1e0),
}

# execute a busca aleatória
n_iter_search = 15
random_search = RandomizedSearchCV(
    clf, param_distributions=param_dist, n_iter=n_iter_search
)

start = time()
random_search.fit(X, y)
print(
    "RandomizedSearchCV levou %.2f segundos para %d configurações de parâmetros candidatos."
    % ((time() - start), n_iter_search)
)

# imprime os resultados
report(random_search.cv_results_)
```
