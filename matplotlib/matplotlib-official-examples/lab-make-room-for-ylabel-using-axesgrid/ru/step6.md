# Создать фигуру с двумя настраиваемыми осями

В этом шаге мы создаем фигуру с двумя настраиваемыми осями. Мы используем метод `make_axes_locatable`, чтобы создать делитель, который позволяет настраивать оси. Мы добавляем новую ось справа от первой оси с использованием метода `append_axes`.

```python
fig = plt.figure()
ax1 = fig.add_axes([0, 0, 1, 1])
divider = make_axes_locatable(ax1)
ax2 = divider.append_axes("right", "100%", pad=0.3, sharey=ax1)
fig.add_axes(ax2)
```
