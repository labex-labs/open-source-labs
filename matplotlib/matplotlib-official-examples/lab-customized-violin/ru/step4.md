# Настройка стиля осей

Наконец, мы настроим стиль для оси x, указав метки делений и пределы. Мы определим вспомогательную функцию `set_axis_style`, чтобы это сделать.

```python
# set style for the axes
labels = ['A', 'B', 'C', 'D']
set_axis_style(ax2, labels)

def set_axis_style(ax, labels):
    ax.set_xticks(np.arange(1, len(labels) + 1))
    ax.set_xticklabels(labels)
    ax.set_xlim(0.25, len(labels) + 0.75)
    ax.set_xlabel('Sample Name')
```
