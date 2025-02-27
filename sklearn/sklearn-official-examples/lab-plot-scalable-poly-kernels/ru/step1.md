# Загрузка и подготовка данных

Сначала мы загрузим датасет Covtype и преобразуем его в задачу бинарной классификации, выбрав только один класс. Затем мы разделим данные на обучающий и тестовый наборы и нормализуем признаки.

```python
from sklearn.datasets import fetch_covtype
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, Normalizer

# Загрузка датасета Covtype, выбор только одного класса
X, y = fetch_covtype(return_X_y=True)
y[y!= 2] = 0
y[y == 2] = 1

# Разделение данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=5000, test_size=10000, random_state=42
)

# Нормализация признаков
mm = make_pipeline(MinMaxScaler(), Normalizer())
X_train = mm.fit_transform(X_train)
X_test = mm.transform(X_test)
```
