# Загрузка датасета

В этом шаге мы загрузим датасет по диабету из библиотеки scikit-learn и стандартизируем данные.

```python
from sklearn import datasets

# Load the diabetes dataset
X, y = datasets.load_diabetes(return_X_y=True)

# Standardize data
X /= X.std(axis=0)
```
