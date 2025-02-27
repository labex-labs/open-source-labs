# Создаем модель SVM с и без разрешения конфликтов (tie-breaking)

В этом шаге мы создадим две модели SVM - одну с отключенным разрешением конфликтов и другую с включенным разрешением конфликтов. Для создания этих моделей мы будем использовать класс `SVC` из scikit - learn. Параметр `break_ties` для двух моделей будет установлен соответственно в `False` и `True`.

```python
for break_ties, title, ax in zip((False, True), titles, sub.flatten()):
    svm = SVC(
        kernel="linear", C=1, break_ties=break_ties, decision_function_shape="ovr"
    ).fit(X, y)
```
