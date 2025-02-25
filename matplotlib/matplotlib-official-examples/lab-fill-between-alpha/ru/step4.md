# Выделение интервалов на осях с использованием `axhspan` и `axvspan`

Еще один удобный способ использования заштрихованных областей - это выделение горизонтальных или вертикальных интервалов на оси. Для этого в Matplotlib есть вспомогательные функции `axhspan` и `axvspan`. См. галерею `axhspan_demo` для получения дополнительной информации.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.axhspan(0.25, 0.75, facecolor='0.5', alpha=0.5)
ax.axvspan(6, 7, facecolor='r', alpha=0.5)

plt.show()
```
