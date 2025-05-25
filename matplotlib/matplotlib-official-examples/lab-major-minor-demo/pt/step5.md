# Seleção automática de ticks para ticks principais e secundários

```python
# Create data
t = np.arange(0.0, 100.0, 0.01)
s = np.sin(2 * np.pi * t) * np.exp(-t * 0.01)

# Plot the data
fig, ax = plt.subplots()
ax.plot(t, s)

# Set the minor locator
ax.xaxis.set_minor_locator(AutoMinorLocator())

# Set the tick parameters
ax.tick_params(which='both', width=2)
ax.tick_params(which='major', length=7)
ax.tick_params(which='minor', length=4, color='r')

# Display the plot
plt.show()
```

Nesta etapa, criamos novos dados e os plotamos. Em seguida, definimos o localizador secundário para selecionar automaticamente o número de ticks secundários. Depois disso, definimos os parâmetros dos ticks, ou seja, a largura e o comprimento dos ticks e sua cor, tanto para os ticks principais quanto para os secundários. Finalmente, exibimos o gráfico.
