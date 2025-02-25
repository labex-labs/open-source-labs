# Nur die äußeren Rahmlinien anzeigen

In diesem Schritt werden wir die Rahmlinien für die inneren Teilplots entfernen und nur die äußeren Rahmlinien anzeigen. Dadurch wird der Plot sauberer aussehen.

```python
for ax in fig.get_axes():
    ss = ax.get_subplotspec()
    ax.spines.top.set_visible(ss.is_first_row())
    ax.spines.bottom.set_visible(ss.is_last_row())
    ax.spines.left.set_visible(ss.is_first_col())
    ax.spines.right.set_visible(ss.is_last_col())
```
