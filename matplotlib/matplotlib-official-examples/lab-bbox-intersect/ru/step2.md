# Настраиваем прямоугольник

Мы определим позицию и размеры прямоугольника с использованием переменных `left`, `bottom`, `width` и `height`. Затем мы создадим прямоугольник с использованием класса `Rectangle` и добавим его на график с использованием метода `add_patch`.

```python
left, bottom, width, height = (-1, -1, 2, 2)
rect = plt.Rectangle((left, bottom), width, height,
                     facecolor="black", alpha=0.1)

fig, ax = plt.subplots()
ax.add_patch(rect)
```
