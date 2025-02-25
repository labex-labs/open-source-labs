# Crear la gráfica

Ahora que tenemos nuestros datos, podemos crear nuestra gráfica utilizando Matplotlib. En este ejemplo, crearemos un diagrama de dispersión utilizando la función `plot()`.

```python
fig, ax = plt.subplots()
plt.plot(x, y, 'o')
```
