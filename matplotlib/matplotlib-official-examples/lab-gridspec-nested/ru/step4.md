# Добавляем подграфики в внутренний gridspec

Теперь мы добавим подграфики в внутренний gridspec. Мы создадим три подграфика: `ax1`, `ax2` и `ax3`.

```python
ax1 = fig.add_subplot(gs00[:-1, :])
ax2 = fig.add_subplot(gs00[-1, :-1])
ax3 = fig.add_subplot(gs00[-1, -1])
```
