# Гауссовская случайная проекция

Теперь давайте применим Гауссовскую случайную проекцию для уменьшения размерности наших данных.

```python
transformer = random_projection.GaussianRandomProjection()
X_new = transformer.fit_transform(X)
```

В этом шаге мы создаем экземпляр класса `GaussianRandomProjection` и настраиваем его на наших данных `X`. Затем мы применяем преобразование, вызвав метод `fit_transform`. Результат сохраняется в переменной `X_new`.
