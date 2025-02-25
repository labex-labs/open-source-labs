# Erstellen der Figur und der Diagramme

```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3], 'ro-', label='easy as 1 2 3')
ax.plot([1, 4, 9], 'gs--', label='easy as 1 2 3 squared')
ax.legend()
```

Wir erstellen eine Figur mit zwei Teilfiguren und plotten zwei Datensätze darauf. Wir fügen auch eine Legende zu den Diagrammen hinzu.
