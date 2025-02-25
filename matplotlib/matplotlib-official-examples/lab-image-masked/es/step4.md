# Creando un gráfico de dispersión

Además de los gráficos de línea, Matplotlib también nos permite crear gráficos de dispersión. Los gráficos de dispersión son útiles para visualizar la relación entre dos variables.

```python
# Create the data
x = np.random.rand(50)
y = np.random.rand(50)

# Create the scatter plot
plt.scatter(x, y)

# Add title and axis labels
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()
```
