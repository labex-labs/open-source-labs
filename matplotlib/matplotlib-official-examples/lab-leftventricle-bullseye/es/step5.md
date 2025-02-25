# Creando un gráfico circular

Crearemos un gráfico circular con cinco porciones que representan diferentes puntos de datos. Utilizaremos la función `pie` proporcionada por el módulo `pyplot` para crear el gráfico circular.

```python
# Creating data for the pie chart
data = [10, 20, 30, 25, 15]

# Creating labels for the pie chart
labels = ['Data 1', 'Data 2', 'Data 3', 'Data 4', 'Data 5']

# Creating a pie chart
plt.pie(data, labels=labels)

# Adding title to the plot
plt.title('Pie Chart')

# Displaying the plot
plt.show()
```
