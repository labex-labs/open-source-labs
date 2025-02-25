# Definir funciones de transformación

El segundo paso es definir las funciones de transformación. En este ejemplo, usaremos la función `tr` para transformar los valores del eje x y dejar los valores del eje y sin cambios. La función `inv_tr` se usará para invertir la transformación.

```python
def tr(x, y):
    return np.sign(x)*abs(x)**.5, y

def inv_tr(x, y):
    return np.sign(x)*x**2, y
```
