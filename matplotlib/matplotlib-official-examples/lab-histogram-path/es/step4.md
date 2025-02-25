# Generar las esquinas de los rectángulos

Para dibujar nuestro histograma usando rectángulos, necesitamos calcular las esquinas de cada rectángulo. Agrega el siguiente código:

```python
left = bins[:-1]
right = bins[1:]
bottom = np.zeros(len(left))
top = bottom + n
```
