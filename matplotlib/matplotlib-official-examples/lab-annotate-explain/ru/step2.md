# Соединить две точки стрелкой

В этом шаге мы соединим две точки стрелкой. Мы будем использовать функцию `annotate` для создания стрелки и настроим стиль и цвет стрелки.

```python
ax = axs.flat[0]
ax.plot([x1, x2], [y1, y2], ".")
ax.annotate("",
            xy=(x1, y1), xycoords='data',
            xytext=(x2, y2), textcoords='data',
            arrowprops=dict(arrowstyle="-",
                            color="0.5",
                            connectionstyle="arc3,rad=0.3",
                            ),
            )
```
