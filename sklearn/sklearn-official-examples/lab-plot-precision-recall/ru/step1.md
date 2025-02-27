# Набор данных и модель

Мы будем использовать набор данных iris и классификатор Linear SVC для дифференциации двух типов ирис. Во - первых, мы импортируем необходимые библиотеки и загружаем набор данных.

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

X, y = load_iris(return_X_y=True)
```

Далее мы добавим шумовые признаки к набору данных и разделим его на обучающую и тестовую выборки.

```python
random_state = np.random.RandomState(0)
n_samples, n_features = X.shape
X = np.concatenate([X, random_state.randn(n_samples, 200 * n_features)], axis=1)

X_train, X_test, y_train, y_test = train_test_split(
    X[y < 2], y[y < 2], test_size=0.5, random_state=random_state
)
```

Наконец, мы масштабируем данные с использованием StandardScaler и подгоняем классификатор Linear SVC к обучающим данным.

```python
classifier = make_pipeline(
    StandardScaler(), LinearSVC(random_state=random_state, dual="auto")
)
classifier.fit(X_train, y_train)
```
