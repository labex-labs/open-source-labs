# Creando un diagrama de dispersión

Crearemos un diagrama de dispersión con valores en el eje X que van desde 0 hasta 5 y valores correspondientes en el eje Y. Utilizaremos la función `scatter` proporcionada por el módulo `pyplot` para crear el diagrama de dispersión.

```python
# Creating X-axis values
x = np.arange(0, 5, 0.1)

# Creating Y-axis values
y = np.sin(x)

# Creating a scatter plot
plt.scatter(x, y)

# Adding title and labels to the plot
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Displaying the plot
plt.show()
```
