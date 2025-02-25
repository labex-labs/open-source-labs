# Добавляем подграфики ко второму внутреннему gridspec

Теперь мы добавим подграфики ко второму внутреннему gridspec. Мы создадим три подграфика: `ax4`, `ax5` и `ax6`.

```python
ax4 = fig.add_subplot(gs01[:, :-1])
ax5 = fig.add_subplot(gs01[:-1, -1])
ax6 = fig.add_subplot(gs01[-1, -1])
```
