# Добавление текста к точечному графику

Теперь мы добавим текст к нашему точечному графику с использованием `offset_copy`. Сначала мы создадим трансформацию, которая позиционирует текст с заданным смещением в координатах экрана относительно заданного места в произвольных координатах. Затем мы будем использовать функцию `text` из `matplotlib.pyplot` для добавления текста к графику.

```python
# Create the transform
trans_offset = mtransforms.offset_copy(ax.transData, fig=fig,
                                       x=0.05, y=0.10, units='inches')

# Add text to the plot
for x, y in zip(xs, ys):
    plt.text(x, y, '%d, %d' % (int(x), int(y)), transform=trans_offset)
```
