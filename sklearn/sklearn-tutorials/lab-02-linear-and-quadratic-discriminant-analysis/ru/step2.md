# Генерация синтетических данных

Далее мы сгенерируем синтетические данные, чтобы продемонстрировать разницу между LDA и QDA. Мы будем использовать функцию `make_classification` из библиотеки scikit-learn для создания двух классов с различными паттернами.

```python
from sklearn.datasets import make_classification

# Generate synthetic data
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, n_classes=2, random_state=1)
```
