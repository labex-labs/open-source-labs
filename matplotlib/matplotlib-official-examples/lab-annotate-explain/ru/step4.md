# Настроить стрелку для соединения с эллипсом

В этом шаге мы настроим стрелку для соединения с эллипсом. Мы будем использовать параметр `arrowprops`, чтобы указать, что стрелка должна соединяться с эллипсом, и также настроим стиль и цвет стрелки.

```python
ax = axs.flat[2]
ax.plot([x1, x2], [y1, y2], ".")
el = mpatches.Ellipse((x1, y1), 0.3, 0.4, angle=30, alpha=0.2)
ax.add_artist(el)
ax.annotate("",
            xy=(x1, y1), xycoords='data',
            xytext=(x2, y2), textcoords='data',
            arrowprops=dict(arrowstyle="-",
                            color="0.5",
                            patchB=el,
                            connectionstyle="arc3,rad=0.3",
                            ),
            )
```
