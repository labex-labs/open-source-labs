# Загрузка данных

Мы загружаем набор данных по диабету из scikit - learn и выводим его описание.

```python
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target
print(diabetes.DESCR)
```
