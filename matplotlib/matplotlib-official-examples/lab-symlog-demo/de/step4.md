# Symlog-Plot auf der x-Achse erstellen

Im ersten Teilplot werden wir einen Symlog-Plot auf der x-Achse erstellen. Wir werden auch ein feines Gitter auf der x-Achse hinzufügen.

```python
ax0.plot(x, y1)
ax0.set_xscale('symlog')
ax0.set_ylabel('symlogx')
ax0.grid()
ax0.xaxis.grid(which='minor')
```
