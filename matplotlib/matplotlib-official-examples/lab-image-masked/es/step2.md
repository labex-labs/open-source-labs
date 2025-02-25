# Creando datos

A continuación, crearemos algunos datos para usar en nuestros gráficos. Para este tutorial, crearemos un gráfico de línea simple.

```python
# Create the data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot the data
plt.plot(x, y)
plt.show()
```
