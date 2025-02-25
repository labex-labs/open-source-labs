# Создать фигуру с двумя осями

В этом шаге мы создаем фигуру с двумя осями. Мы используем метод `add_axes`, чтобы добавить две оси к фигуре. Также мы задаем метку деления оси Y для первой оси и заголовок для второй оси.

```python
fig = plt.figure()
ax1 = fig.add_axes([0, 0, 1, 0.5])
ax2 = fig.add_axes([0, 0.5, 1, 0.5])

ax1.set_yticks([0.5], labels=["very long label"])
ax1.set_ylabel("Y label")

ax2.set_title("Title")
```
