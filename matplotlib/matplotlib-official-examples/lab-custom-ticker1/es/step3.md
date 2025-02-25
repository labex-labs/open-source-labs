# Crear la gráfica

Ahora, podemos crear la gráfica con el cotizador personalizado. Crearemos un gráfico de barras con datos de muestra y configuraremos el cotizador del eje y para que utilice nuestra función de cotizador personalizada.

```python
# Create a bar chart with sample data
fig, ax = plt.subplots()
money = [1.5e5, 2.5e6, 5.5e6, 2.0e7]
ax.bar(['Bill', 'Fred', 'Mary', 'Sue'], money)

# Set the y-axis ticker to use the custom ticker function
ax.yaxis.set_major_formatter(ticker.FuncFormatter(millions))

# Display the plot
plt.show()
```
