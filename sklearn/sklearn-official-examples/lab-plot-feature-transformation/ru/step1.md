# Подготовка данных

Во - первых, мы создадим большой датасет из 80 000 образцов и разделим его на три множества:

- Множество для обучения ансамблевых методов, которые впоследствии будут использоваться в качестве трансформера для инженерных преобразований признаков
- Множество для обучения линейной модели
- Множество для тестирования линейной модели.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=80_000, random_state=10)

X_full_train, X_test, y_full_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=10
)

X_train_ensemble, X_train_linear, y_train_ensemble, y_train_linear = train_test_split(
    X_full_train, y_full_train, test_size=0.5, random_state=10
)
```
