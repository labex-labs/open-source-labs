# Crear un gráfico de barras

En este paso, crearemos un gráfico de barras utilizando Matplotlib. Comenzaremos generando algunos datos para graficar utilizando la función `random()` de NumPy. Luego, utilizaremos la función `bar()` para crear el gráfico.

```python
x = ['A', 'B', 'C', 'D', 'E']
y = np.random.randint(1, 10, 5)

plt.bar(x, y)
plt.show()
```
