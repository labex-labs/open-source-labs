# Генерация данных

Мы сгенерируем синтетический датасет с только 3 информативными признаками. Мы явно не перемешаем датасет, чтобы убедиться, что информативные признаки соответствуют первым трем столбцам X. Кроме того, мы разделим наш датасет на тренировочную и тестовую подмножества.

```python
X, y = make_classification(
    n_samples=1000,
    n_features=10,
    n_informative=3,
    n_redundant=0,
    n_repeated=0,
    n_classes=2,
    random_state=0,
    shuffle=False,
)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
```
