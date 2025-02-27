# Определение пространства параметров

Определите словарь `param_dist`, который содержит гиперпараметры и их соответствующие значения для поиска. Гиперпараметры: `max_depth`, `max_features`, `min_samples_split`, `bootstrap` и `criterion`. Диапазон поиска для `max_features` и `min_samples_split` определяется с использованием функции `randint` из модуля `scipy.stats`. Код для определения пространства параметров выглядит следующим образом:

```python
param_dist = {
    "max_depth": [3, None],
    "max_features": randint(1, 6),
    "min_samples_split": randint(2, 11),
    "bootstrap": [True, False],
    "criterion": ["gini", "entropy"],
}
```
