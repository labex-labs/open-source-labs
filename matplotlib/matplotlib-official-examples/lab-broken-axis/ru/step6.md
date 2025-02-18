# Скрытие осевых линий (spines)

Теперь мы скроем осевые линии между двумя подграфиками, используя `ax1.spines.bottom.set_visible` и `ax2.spines.top.set_visible`.

```python
ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)
```
