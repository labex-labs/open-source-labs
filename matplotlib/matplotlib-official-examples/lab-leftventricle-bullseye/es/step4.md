# Creando un diagrama de barras

Crearemos un diagrama de barras con valores en el eje X que van desde 0 hasta 5 y valores correspondientes en el eje Y. Utilizaremos la función `bar` proporcionada por el módulo `pyplot` para crear el diagrama de barras.

```python
# Creating X-axis values
x = np.arange(0, 5, 0.1)

# Creating Y-axis values
y = np.sin(x)

# Creating a bar plot
plt.bar(x, y)

# Adding title and labels to the plot
plt.title('Bar Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Displaying the plot
plt.show()
```
