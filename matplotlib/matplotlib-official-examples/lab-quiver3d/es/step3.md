# Definir la dirección de las flechas

Ahora definiremos la dirección de las flechas. En este ejemplo, definiremos la dirección de las flechas utilizando las funciones trigonométricas de NumPy. Las funciones `sin` y `cos` se utilizan para crear las matrices `u`, `v` y `w` que representan la dirección de las flechas en las direcciones `x`, `y` y `z`.

```python
u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
     np.sin(np.pi * z))
```
