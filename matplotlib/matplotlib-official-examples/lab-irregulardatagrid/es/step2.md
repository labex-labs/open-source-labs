# Generar datos aleatorios

Generamos datos aleatorios utilizando el método `np.random.uniform` de NumPy. Generamos `npts = 200` puntos de datos con valores de x e y entre -2 y 2. También calculamos los valores de z utilizando la función `z = x * np.exp(-x**2 - y**2)`.

```python
np.random.seed(19680801)
npts = 200
x = np.random.uniform(-2, 2, npts)
y = np.random.uniform(-2, 2, npts)
z = x * np.exp(-x**2 - y**2)
```
