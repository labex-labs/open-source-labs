# Asignar las líneas de la leyenda a las líneas originales

Asignaremos las líneas de la leyenda a las líneas originales utilizando un diccionario.

```python
lines = [line1, line2]
lined = {}  # Asignará las líneas de la leyenda a las líneas originales.
for legline, origline in zip(leg.get_lines(), lines):
    legline.set_picker(True)  # Habilita la selección en la línea de la leyenda.
    lined[legline] = origline
```
