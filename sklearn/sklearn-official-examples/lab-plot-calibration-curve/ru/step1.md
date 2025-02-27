# Набор данных

Мы будем использовать синтетический бинарный набор данных для классификации с 100 000 образцами и 20 признаками. Из 20 признаков только 2 информативны, 10 являются избыточными (случайными комбинациями информативных признаков), а оставшиеся 8 не информативны (случайные числа). Из 100 000 образцов 1 000 будут использоваться для настройки модели, а остальные для тестирования.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_samples=100_000, n_features=20, n_informative=2, n_redundant=10, random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.99, random_state=42
)
```
