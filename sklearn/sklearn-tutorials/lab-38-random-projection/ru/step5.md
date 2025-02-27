# Обратное преобразование

Трансформеры случайной проекции имеют возможность вычислить обратную матрицу проекции. Давайте исследуем эту функцию, применяя обратное преобразование к нашим проектированным данным.

```python
transformer = random_projection.SparseRandomProjection(compute_inverse_components=True)
X_new = transformer.fit_transform(X)

# Compute the inverse transform
X_new_inversed = transformer.inverse_transform(X_new)
```

В этом шаге мы создаем экземпляр класса `SparseRandomProjection` с параметром `compute_inverse_components`, установленным в `True`. Затем мы настраиваем трансформер на наших данных `X` и применяем преобразование. Наконец, мы вычисляем обратное преобразование, вызвав метод `inverse_transform` для проектированных данных `X_new`.
