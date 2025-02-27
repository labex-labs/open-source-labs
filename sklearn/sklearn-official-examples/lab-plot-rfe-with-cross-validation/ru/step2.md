# Обучение и выбор модели

Мы создадим объект RFECV и вычислим кросс-валидированные оценки. Стратегия оценивания "accuracy" оптимизирует долю правильно классифицированных выборок. Мы будем использовать логистическую регрессию в качестве оценщика и стратифицированную k-кратную кросс-валидацию с 5 фолдами.

```python
from sklearn.feature_selection import RFECV
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression

min_features_to_select = 1  # Минимальное количество признаков для рассмотрения
clf = LogisticRegression()
cv = StratifiedKFold(5)

rfecv = RFECV(
    estimator=clf,
    step=1,
    cv=cv,
    scoring="accuracy",
    min_features_to_select=min_features_to_select,
    n_jobs=2,
)
rfecv.fit(X, y)

print(f"Optimal number of features: {rfecv.n_features_}")
```
