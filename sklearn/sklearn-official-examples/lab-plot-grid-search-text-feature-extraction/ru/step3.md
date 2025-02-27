# Настройка гиперпараметров

Мы используем RandomizedSearchCV для исследования сетки гиперпараметров и нахождения наилучшей комбинации гиперпараметров для конвейера (pipeline). В данном случае мы устанавливаем n_iter=40, чтобы ограничить пространство поиска. Мы можем увеличить значение n_iter, чтобы получить более информативный анализ, но это увеличит время вычислений.

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

print("Performing grid search...")
print("Hyperparameters to be evaluated:")
pprint(parameter_grid)

random_search.fit(data_train.data, data_train.target)

test_accuracy = random_search.score(data_test.data, data_test.target)

```
