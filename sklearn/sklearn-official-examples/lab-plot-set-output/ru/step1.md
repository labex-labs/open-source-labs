# Загрузка датасета Iris

Сначала мы загрузим датасет Iris в виде DataFrame, чтобы продемонстрировать API `set_output`.

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

X, y = load_iris(as_frame=True, return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)
X_train.head()
```
