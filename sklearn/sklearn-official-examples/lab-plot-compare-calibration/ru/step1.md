# Импортируем библиотеки и генерируем датасет

Начнем с импорта необходимых библиотек и генерации синтетического бинарного датасета классификации с 100 000 образцами и 20 признаками. Из 20 признаков только 2 информативны, 2 избыточны, а оставшиеся 16 не несут информации. Из 100 000 образцов 100 будут использоваться для настройки модели, а остальные для тестирования.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Generate dataset
X, y = make_classification(
    n_samples=100_000, n_features=20, n_informative=2, n_redundant=2, random_state=42
)

train_samples = 100  # Samples used for training the models
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    shuffle=False,
    test_size=100_000 - train_samples
)
```
