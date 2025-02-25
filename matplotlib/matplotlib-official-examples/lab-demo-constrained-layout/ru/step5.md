# Создание вложенных GridSpec сConstrained Layout

Мы создаем более сложный пример, используя вложенные GridSpec с _constrained layout_. Это позволяет нам иметь больше контроля над макетом подграфиков.

```python
fig = plt.figure(layout='constrained')

gs0 = gridspec.GridSpec(1, 2, figure=fig)

gs1 = gridspec.GridSpecFromSubplotSpec(3, 1, subplot_spec=gs0[0])
for n in range(3):
    ax = fig.add_subplot(gs1[n])
    example_plot(ax)


gs2 = gridspec.GridSpecFromSubplotSpec(2, 1, subplot_spec=gs0[1])
for n in range(2):
    ax = fig.add_subplot(gs2[n])
    example_plot(ax)

plt.show()
```
