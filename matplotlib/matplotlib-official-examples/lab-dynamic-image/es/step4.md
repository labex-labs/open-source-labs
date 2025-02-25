# Generar los datos

Utilizaremos el método `linspace` de la biblioteca Numpy para generar los datos de la animación. Generaremos dos conjuntos de datos, `x` e `y`, y luego redimensionaremos los datos de `y` para crear una matriz bidimensional.

```python
x = np.linspace(0, 2 * np.pi, 120)
y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
```
