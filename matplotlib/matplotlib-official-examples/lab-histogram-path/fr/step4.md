# Générez les coins des rectangles

Pour tracer notre histogramme à l'aide de rectangles, nous devons calculer les coins de chaque rectangle. Ajoutez le code suivant :

```python
left = bins[:-1]
right = bins[1:]
bottom = np.zeros(len(left))
top = bottom + n
```
