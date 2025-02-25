# Creando un diagrama de líneas simple

Crearemos un diagrama de líneas simple con valores en el eje X que van desde 0 hasta 5 y valores correspondientes en el eje Y. Utilizaremos la función `plot` proporcionada por el módulo `pyplot` para crear el diagrama de líneas.

```python
# Creating X-axis values
x = np.arange(0, 5, 0.1)

# Creating Y-axis values
y = np.sin(x)

# Creating a line plot
plt.plot(x, y)

# Adding title and labels to the plot
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Displaying the plot
plt.show()
```
