# Diagramm mit `.step()` erstellen

Wir können die `.step()`-Funktion verwenden, um stückweise konstante Kurven zu erstellen. Der `where`-Parameter bestimmt, wo die Schritte gezeichnet werden sollen. Wir werden drei Diagramme mit unterschiedlichen Werten für `where` erstellen.

```python
plt.step(x, y + 2, label='pre (default)', where='pre')
plt.step(x, y + 1, label='mid', where='mid')
plt.step(x, y, label='post', where='post')
plt.legend()
plt.show()
```

Der obige Code wird ein Diagramm mit drei stückweise konstanten Kurven erstellen, wobei jeder eine unterschiedliche `where`-Wert hat.
