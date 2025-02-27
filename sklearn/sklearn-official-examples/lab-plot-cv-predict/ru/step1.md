# Загрузка и подготовка данных

Сначала мы загрузим датасет по диабету и подготовим его для моделирования. Мы будем использовать функцию `load_diabetes` из библиотеки scikit-learn для загрузки датасета в два массива: `X` и `y`.

```python
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True)
```
