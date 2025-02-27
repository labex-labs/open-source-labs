# Загружаем датасет и определяем параметры для GridSearchCV

Мы загрузим датасет digits и определим параметры для GridSearchCV. Мы установим параметр для усечения PCA и регуляризации классификатора.

```python
X_digits, y_digits = datasets.load_digits(return_X_y=True)

param_grid = {
    "pca__n_components": [5, 15, 30, 45, 60],
    "logistic__C": np.logspace(-4, 4, 4),
}
```
