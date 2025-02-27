# Обучение и выбор модели

Мы изменяем количество компонентов от 1 до 6 и тип параметров ковариации для использования:

- `"full"` (полный): каждая компонента имеет свою собственную общую матрицу ковариации.
- `"tied"` (общий): все компоненты используют одну и ту же общую матрицу ковариации.
- `"diag"` (диагональный): каждая компонента имеет свою собственную диагональную матрицу ковариации.
- `"spherical"` (сферический): каждая компонента имеет свою собственную единичную дисперсию.

Мы оцениваем разные модели и выбираем наилучшую (с наим. значением BIC). Это делается с использованием `GridSearchCV` и пользовательской функции оценки, которая возвращает отрицательный показатель BIC. Лучшие параметры и оценщик сохраняются в `best_parameters_` и `best_estimator_` соответственно.

```python
from sklearn.mixture import GaussianMixture
from sklearn.model_selection import GridSearchCV

def gmm_bic_score(estimator, X):
    """Callable to pass to GridSearchCV that will use the BIC score."""
    # Make it negative since GridSearchCV expects a score to maximize
    return -estimator.bic(X)

param_grid = {
    "n_components": range(1, 7),
    "covariance_type": ["spherical", "tied", "diag", "full"],
}
grid_search = GridSearchCV(
    GaussianMixture(), param_grid=param_grid, scoring=gmm_bic_score
)
grid_search.fit(X)
```
