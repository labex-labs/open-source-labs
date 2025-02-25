# Erstellen eines 3D-Diagramms

Als nächstes erstellen wir ein 3D-Diagramm, indem wir die `add_subplot`-Methode des `figure`-Objekts verwenden. Wir legen den `projection`-Parameter auf `'3d'` fest, um anzugeben, dass wir ein 3D-Diagramm möchten.

```python
ax = plt.figure().add_subplot(projection='3d')
```
