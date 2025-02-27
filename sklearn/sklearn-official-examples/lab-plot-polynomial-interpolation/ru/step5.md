# Периодические сплайны

Мы демонстрируем использование периодических сплайнов с помощью `SplineTransformer` и ручного указания узлов. Мы подгоняем модель регрессии с регуляризацией к тренировочным данным и строим график функции, тренировочных точек и интерполяцию с использованием периодических сплайнов.

```python
def g(x):
    """Функция, которая будет аппроксимироваться периодической интерполяцией сплайнов."""
    return np.sin(x) - 0.7 * np.cos(x * 3)


y_train = g(x_train)

# Продлеваем тестовые данные в будущее:
x_plot_ext = np.linspace(-1, 21, 200)
X_plot_ext = x_plot_ext[:, np.newaxis]

lw = 2
fig, ax = plt.subplots()
ax.set_prop_cycle(color=["black", "tomato", "teal"])
ax.plot(x_plot_ext, g(x_plot_ext), linewidth=lw, label="исходная функция")
ax.scatter(x_train, y_train, label="тренировочные точки")

for transformer, label in [
    (SplineTransformer(degree=3, n_knots=10), "сплайн"),
    (
        SplineTransformer(
            degree=3,
            knots=np.linspace(0, 2 * np.pi, 10)[:, None],
            extrapolation="periodic",
        ),
        "периодический сплайн",
    ),
]:
    model = make_pipeline(transformer, Ridge(alpha=1e-3))
    model.fit(X_train, y_train)
    y_plot_ext = model.predict(X_plot_ext)
    ax.plot(x_plot_ext, y_plot_ext, label=label)

ax.legend()
fig.show()
```
