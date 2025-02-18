# Festlegen der y-Achsengrenzen

Wir werden die y-Achse des ersten Teilplots (Subplots) so begrenzen, dass nur die Ausreißer angezeigt werden, und die des zweiten Teilplots, um die Mehrheit der Daten anzuzeigen. Wir verwenden `ax1.set_ylim` und `ax2.set_ylim`, um die y-Achsengrenzen festzulegen.

```python
ax1.set_ylim(.78, 1.)  # nur Ausreißer
ax2.set_ylim(0,.22)  # die meisten Daten
```
