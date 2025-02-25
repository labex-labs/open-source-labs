# Creando el círculo

Crearemos el círculo usando la función `make_circle()`. La función toma el radio del círculo como entrada y devuelve las coordenadas x e y del círculo.

```python
def make_circle(r):
    t = np.arange(0, np.pi * 2.0, 0.01)
    t = t.reshape((len(t), 1))
    x = r * np.cos(t)
    y = r * np.sin(t)
    return np.hstack((x, y))
```
