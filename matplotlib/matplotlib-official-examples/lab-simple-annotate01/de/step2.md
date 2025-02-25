# Ein Diagramm erstellen

Wir werden nun ein Diagramm erstellen, dem wir Anmerkungen hinzufügen wollen. Der folgende Code erstellt ein Diagramm mit zwei Datenpunkten.

```python
fig, ax = plt.subplots()
x = [1, 2]
y = [3, 4]
ax.plot(x, y, "o")
```
