# Crear las subfiguras y llamar a la función `test_rotation_mode`

Crearemos dos subfiguras y llamaremos a la función `test_rotation_mode` con los parámetros `fig` y `mode`.

```python
fig = plt.figure(figsize=(8, 5))
subfigs = fig.subfigures(1, 2)
test_rotation_mode(subfigs[0], "default")
test_rotation_mode(subfigs[1], "anchor")
plt.show()
```
