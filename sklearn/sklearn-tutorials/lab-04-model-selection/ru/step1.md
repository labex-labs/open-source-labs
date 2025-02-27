# Оценка и оценки при кросс-валидации

Оценивающие инструменты в scikit-learn предоставляют метод `score`, который можно использовать для оценки качества подгонки модели или предсказания на новых данных. Этот метод возвращает оценку, при этом более высокое значение указывает на лучшую производительность.

```python
from sklearn import datasets, svm

# Загрузить набор данных цифр
X_digits, y_digits = datasets.load_digits(return_X_y=True)

# Создать классификатор SVM с линейным ядром
svc = svm.SVC(C=1, kernel='linear')

# Подогнать классификатор к тренировочным данным и вычислить оценку на тестовых данных
score = svc.fit(X_digits[:-100], y_digits[:-100]).score(X_digits[-100:], y_digits[-100:])
```

Для получения более точной оценки точности предсказания можно использовать кросс-валидацию. Кросс-валидация заключается в разделении данных на несколько фолдов, использовании каждого фолда в качестве тестового набора и оставшихся фолдов в качестве тренировочных наборов. Этот процесс повторяется несколько раз, и оценки усредняются, чтобы получить общую производительность.

```python
import numpy as np

# Разделить данные на 3 фолда
X_folds = np.array_split(X_digits, 3)
y_folds = np.array_split(y_digits, 3)

# Выполнить кросс-валидацию
scores = []
for k in range(3):
    X_train = list(X_folds)
    X_test = X_train.pop(k)
    X_train = np.concatenate(X_train)
    y_train = list(y_folds)
    y_test = y_train.pop(k)
    y_train = np.concatenate(y_train)
    scores.append(svc.fit(X_train, y_train).score(X_test, y_test))

print(scores)
```
