# Интерполяция B-сплайнами

Мы будем использовать `SplineTransformer` для генерации базисных функций B-сплайна и подгонки модели регрессии с регуляризацией к тренировочным данным. Затем построим график функции, тренировочных точек и интерполяцию с использованием B-сплайнов.

```python
# B-сплайн с 4 + 3 - 1 = 6 базисными функциями
model = make_pipeline(SplineTransformer(n_knots=4, degree=3), Ridge(alpha=1e-3))
model.fit(X_train, y_train)

y_plot = model.predict(X_plot)
ax.plot(x_plot, y_plot, label="B-spline")
ax.legend(loc="lower center")
ax.set_ylim(-20, 10)
plt.show()
```
