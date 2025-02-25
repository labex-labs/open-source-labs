# Definir los valores de x, y y z

Generaremos los valores de x, y y z utilizando NumPy. Primero definiremos el rango de valores para theta y z. Luego, utilizaremos estos valores para generar los valores de r, x e y.

```python
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
```
