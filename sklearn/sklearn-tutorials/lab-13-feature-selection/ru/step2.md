# Выбор признаков с использованием одномерных статистик

Выбор признаков с использованием одномерных статистик заключается в выборе наилучших признаков на основе одномерных статистических тестов. В scikit-learn есть несколько классов, которые реализуют выбор признаков с использованием одномерных статистик:

- `SelectKBest`: выбирает топ-k признаков с наивысшими оценками
- `SelectPercentile`: выбирает заданный пользователем процент признаков с наивысшими оценками
- `SelectFpr`: выбирает признаки на основе уровня ложноположительных результатов (false positive rate)
- `SelectFdr`: выбирает признаки на основе уровня ложных обнаружений (false discovery rate)
- `SelectFwe`: выбирает признаки на основе семейного уровня ошибок (family wise error)
- `GenericUnivariateSelect`: позволяет выбирать признаки с конфигурируемой стратегией

Вот пример использования `SelectKBest` для выбора двух наилучших признаков из набора данных Iris:

```python
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

# Load the Iris dataset
X, y = load_iris(return_X_y=True)

# Initialize SelectKBest with the f_classif scoring function and k=2
selector = SelectKBest(f_classif, k=2)

# Select the best features
X_selected = selector.fit_transform(X, y)

print("Original X shape:", X.shape)
print("X with selected features shape:", X_selected.shape)
print("Selected features:", selector.get_support(indices=True))
```

В этом примере мы используем функцию оценки `f_classif` и выбираем два наилучших признака из набора данных Iris. Вывод покажет исходную форму набора данных и форму после выбора наилучших признаков.
