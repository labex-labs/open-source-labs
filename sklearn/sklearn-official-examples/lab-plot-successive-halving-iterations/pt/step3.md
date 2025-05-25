# Definindo o Espaço de Parâmetros

Defina um dicionário `param_dist` que contém os hiperparâmetros e seus respectivos valores para serem pesquisados. Os hiperparâmetros são `max_depth`, `max_features`, `min_samples_split`, `bootstrap` e `criterion`. O intervalo de busca para `max_features` e `min_samples_split` é definido usando a função `randint` do módulo `scipy.stats`. O código para definir o espaço de parâmetros é o seguinte:

```python
param_dist = {
    "max_depth": [3, None],
    "max_features": randint(1, 6),
    "min_samples_split": randint(2, 11),
    "bootstrap": [True, False],
    "criterion": ["gini", "entropy"],
}
```
