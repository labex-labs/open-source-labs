# Обучаем модели изотонной и линейной регрессии

Теперь мы обучим обе модели: изотонную и линейную регрессию на сгенерированных данных.

```python
ir = IsotonicRegression(out_of_bounds="clip")
y_ = ir.fit_transform(x, y)

lr = LinearRegression()
lr.fit(x[:, np.newaxis], y)  # x needs to be 2d for LinearRegression
```
