# Erstellen des polaren Diagramms

Jetzt können wir das polare Diagramm erstellen, indem wir den Parameter `subplot_kw` verwenden, um den Projektionstyp als 'polar' anzugeben.

```python
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
```
