# Definir los datos

A continuación, necesitamos definir los datos que utilizaremos para nuestro diagrama. Crearemos una onda sinusoidal con 201 puntos de datos:

```python
t = np.linspace(0.0, 2.0, 201)
s = np.sin(2 * np.pi * t)
```
