# Экстремальные оценщики с кросс-валидацией

Некоторые оценщики в scikit-learn обладают встроенными возможностями кросс-валидации. Эти оценщики с кросс-валидацией автоматически выбирают свои параметры с использованием кросс-валидации, что делает процесс выбора модели более эффективным.

```python
from sklearn import linear_model, datasets

# Создать объект LassoCV
lasso = linear_model.LassoCV()

# Загрузить набор данных по диабету
X_diabetes, y_diabetes = datasets.load_diabetes(return_X_y=True)

# Подогнать объект LassoCV к набору данных
lasso.fit(X_diabetes, y_diabetes)

print(lasso.alpha_)
```
