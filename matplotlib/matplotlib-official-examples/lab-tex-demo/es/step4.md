# Crear un diagrama de dispersión

En este paso, crearemos un diagrama de dispersión utilizando Matplotlib. Comenzaremos generando algunos datos aleatorios para graficar utilizando la función `random()` de NumPy. Luego, utilizaremos la función `scatter()` para crear el gráfico.

```python
x = np.random.randn(100)
y = np.random.randn(100)

plt.scatter(x, y)
plt.show()
```
