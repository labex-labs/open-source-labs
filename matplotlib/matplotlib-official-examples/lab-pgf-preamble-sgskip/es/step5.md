# Crear un gráfico de dispersión

Además de los gráficos de línea, Matplotlib también puede crear gráficos de dispersión. Aquí hay un ejemplo:

```python
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 500 * np.random.rand(50)

plt.scatter(x, y, c=colors, s=sizes)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')
plt.show()
```
