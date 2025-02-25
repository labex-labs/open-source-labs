# Erzeuge die Figur- und Achsenobjekte

Wir werden nun die Figur- und Achsenobjekte mit der Methode `add_subplot()` erstellen. Wir werden den Parameter `projection` auf `'3d'` setzen, um einen 3D-Graphen zu erstellen.

```python
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
```
