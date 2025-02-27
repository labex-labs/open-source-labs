# Предварительная обработка данных

Первым шагом является предварительная обработка набора данных. В этом примере мы используем реальные-world наборы данных, доступные в модуле `datasets` Scikit-Learn. Размер выборки некоторых наборов данных уменьшается, чтобы ускорить вычисления. После предварительной обработки данных, целевые переменные наборов данных будут иметь два класса, 0, представляющий нормальные объекты, и 1, представляющий выбросы. Функция `preprocess_dataset` возвращает данные и целевую переменную.

```python
import numpy as np
from sklearn.datasets import fetch_kddcup99, fetch_covtype, fetch_openml
from sklearn.preprocessing import LabelBinarizer
import pandas as pd

rng = np.random.RandomState(42)

def preprocess_dataset(dataset_name):
    # загрузка и векторизация
    print(f"Загрузка данных {dataset_name}")
    if dataset_name in ["http", "smtp", "SA", "SF"]:
        dataset = fetch_kddcup99(subset=dataset_name, percent10=True, random_state=rng)
        X = dataset.data
        y = dataset.target
        lb = LabelBinarizer()

        if dataset_name == "SF":
            idx = rng.choice(X.shape[0], int(X.shape[0] * 0.1), replace=False)
            X = X[idx]  # уменьшить размер выборки
            y = y[idx]
            x1 = lb.fit_transform(X[:, 1].astype(str))
            X = np.c_[X[:, :1], x1, X[:, 2:]]
        elif dataset_name == "SA":
            idx = rng.choice(X.shape[0], int(X.shape[0] * 0.1), replace=False)
            X = X[idx]  # уменьшить размер выборки
            y = y[idx]
            x1 = lb.fit_transform(X[:, 1].astype(str))
            x2 = lb.fit_transform(X[:, 2].astype(str))
            x3 = lb.fit_transform(X[:, 3].astype(str))
            X = np.c_[X[:, :1], x1, x2, x3, X[:, 4:]]
        y = (y!= b"normal.").astype(int)
    if dataset_name == "forestcover":
        dataset = fetch_covtype()
        X = dataset.data
        y = dataset.target
        idx = rng.choice(X.shape[0], int(X.shape[0] * 0.1), replace=False)
        X = X[idx]  # уменьшить размер выборки
        y = y[idx]

        # нормальные объекты - те, у которых атрибут 2
        # выбросы - те, у которых атрибут 4
        s = (y == 2) + (y == 4)
        X = X[s, :]
        y = y[s]
        y = (y!= 2).astype(int)
    if dataset_name in ["glass", "wdbc", "cardiotocography"]:
        dataset = fetch_openml(
            name=dataset_name, version=1, as_frame=False, parser="pandas"
        )
        X = dataset.data
        y = dataset.target

        if dataset_name == "glass":
            s = y == "tableware"
            y = s.astype(int)
        if dataset_name == "wdbc":
            s = y == "2"
            y = s.astype(int)
            X_mal, y_mal = X[s], y[s]
            X_ben, y_ben = X[~s], y[~s]

            # уменьшено до 39 точек (9,8% выбросов)
            idx = rng.choice(y_mal.shape[0], 39, replace=False)
            X_mal2 = X_mal[idx]
            y_mal2 = y_mal[idx]
            X = np.concatenate((X_ben, X_mal2), axis=0)
            y = np.concatenate((y_ben, y_mal2), axis=0)
        if dataset_name == "cardiotocography":
            s = y == "3"
            y = s.astype(int)
    # 0 представляет нормальные объекты, а 1 - выбросы
    y = pd.Series(y, dtype="category")
    return (X, y)
```
