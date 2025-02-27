# Применение GridSearchCV

Далее мы применим GridSearchCV, чтобы найти наилучшее значение альфа для регрессии Lasso. Мы будем использовать диапазон значений альфа от 10^-4 до 10^-0.5 с 30 значениями между ними. Мы будем использовать 5 фолдов для кросс-валидации.

```python
from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV

lasso = Lasso(random_state=0, max_iter=10000)
alphas = np.logspace(-4, -0.5, 30)

tuned_parameters = [{"alpha": alphas}]
n_folds = 5

clf = GridSearchCV(lasso, tuned_parameters, cv=n_folds, refit=False)
clf.fit(X, y)
```
