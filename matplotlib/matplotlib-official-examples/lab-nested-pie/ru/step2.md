# Создаем вложенную круговую диаграмму с использованием `ax.pie`

Мы можем создать вложенную круговую диаграмму с использованием метода `ax.pie`. Сначала мы сгенерируем некоторые фальшивые данные, соответствующие трем группам. В внутреннем круге мы будем рассматривать каждое число как принадлежащее своей собственной группе. В внешнем круге мы будем отображать их как членов их исходных трех групп.

```python
fig, ax = plt.subplots()

size = 0.3
vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

cmap = plt.colormaps["tab20c"]
outer_colors = cmap(np.arange(3)*4)
inner_colors = cmap([1, 2, 5, 6, 9, 10])

ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
       wedgeprops=dict(width=size, edgecolor='w'))

ax.pie(vals.flatten(), radius=1-size, colors=inner_colors,
       wedgeprops=dict(width=size, edgecolor='w'))

ax.set(aspect="equal", title='Pie plot with `ax.pie`')
plt.show()
```
