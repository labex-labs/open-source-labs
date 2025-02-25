# Добавление погрешностных полос на график

Мы добавляем погрешностные полосы на наш график, используя метод `errorbar` объекта `Axes3D`. Мы задаем параметры `zuplims` и `zlolims` массивами, которые определяют, какие точки данных имеют верхние и нижние пределы. Мы задаем параметр `errorevery`, чтобы контролировать частоту появления погрешностных полос.

```python
estep = 15
i = np.arange(t.size)
zuplims = (i % estep == 0) & (i // estep % 3 == 0)
zlolims = (i % estep == 0) & (i // estep % 3 == 2)

ax.errorbar(x, y, z, 0.2, zuplims=zuplims, zlolims=zlolims, errorevery=estep)
```
