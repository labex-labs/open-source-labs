# Fortgeschrittene Balkenbeschriftung

In diesem Schritt zeigen wir einige weitere fortgeschrittene Dinge, die mit Balkenbeschriftungen möglich sind. Wir verwenden das gleiche horizontale Balkendiagramm wie im vorherigen Schritt.

```python
fig, ax = plt.subplots()

hbars = ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

# Label with given captions, custom padding and annotate options
ax.bar_label(hbars, labels=[f'±{e:.2f}' for e in error],
             padding=8, color='b', fontsize=14)
ax.set_xlim(right=16)

plt.show()
```
