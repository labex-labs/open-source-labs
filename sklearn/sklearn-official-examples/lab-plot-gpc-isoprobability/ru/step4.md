# Оценка модели

Мы оценим производительность классификации обученной модели GPC. Мы сгенерируем сетку точек и вычислим предсказанные вероятности для каждой точки с использованием обученной модели.

```python
# Evaluate real function and the predicted probability
res = 50
x1, x2 = np.meshgrid(np.linspace(-lim, lim, res), np.linspace(-lim, lim, res))
xx = np.vstack([x1.reshape(x1.size), x2.reshape(x2.size)]).T

y_true = g(xx)
y_prob = gp.predict_proba(xx)[:, 1]
y_true = y_true.reshape((res, res))
y_prob = y_prob.reshape((res, res))
```
