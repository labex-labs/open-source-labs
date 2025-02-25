# Funktion zum Aktualisieren des Titels definieren

Definieren Sie die Funktion, um den Titel der Abbildung mit der aktuellen Zeit zu aktualisieren.

```python
def update_title(axes):
    axes.set_title(datetime.now())
    axes.figure.canvas.draw()
```
