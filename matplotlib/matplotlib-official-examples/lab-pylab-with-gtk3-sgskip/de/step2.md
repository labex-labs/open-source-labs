# Figur und Achse erstellen

Als nächstes werden wir eine Figur und eine Achse mit der `subplots()`-Methode erstellen. Anschließend werden wir zwei Linien auf der Achse plotten und eine Legende hinzufügen, um sie voneinander zu unterscheiden.

```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3], 'ro-', label='easy as 1 2 3')
ax.plot([1, 4, 9], 'gs--', label='easy as 1 2 3 squared')
ax.legend()
```
