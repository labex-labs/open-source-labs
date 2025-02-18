# Oberer Titel

Erstellen Sie ein Diagramm mit einem Titel oben, indem Sie die Funktion `subplots()` und die Funktion `set_xlabel()` verwenden.

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.xaxis.set_label_position('top')
ax.set_xlabel('X-label')
ax.set_title('Top Title')
```
