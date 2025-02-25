# Настраиваем подграфики

Мы настраиваем подграфики, устанавливая цвет фона нижних подграфиков в черный, настраивая деления на оси x и добавляя заголовок к каждому подграфику.

```python
axs[1, icol].set_facecolor('k')
axs[1, icol].xaxis.set_ticks(np.arange(0, 10, 2))
axs[0, icol].set_title(f'line widths (pts): {lwx:g}, {lwy:g}',
                       fontsize='medium')
```
