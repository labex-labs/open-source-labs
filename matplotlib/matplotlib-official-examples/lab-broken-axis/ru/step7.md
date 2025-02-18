# Настройка делений (ticks)

Теперь мы настроим деления на оси x. Мы переместим деления на первом подграфике вверх, используя `ax1.xaxis.tick_top`, удалим подписи к делениям на первом подграфике с помощью `ax1.tick_params(labeltop=False)` и оставим подписи к делениям на втором подграфике.

```python
ax1.xaxis.tick_top()
ax1.tick_params(labeltop=False)
ax2.xaxis.tick_bottom()
```
