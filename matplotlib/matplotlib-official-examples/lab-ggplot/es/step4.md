# Crear gráficos de barras

Vamos a crear gráficos de barras con puntos de datos aleatorios.

```python
# Create bar graphs
x = np.arange(5)
y1, y2 = np.random.randint(1, 25, size=(2, 5))
width = 0.25

plt.bar(x, y1, width)
plt.bar(x + width, y2, width, color=list(plt.rcParams['axes.prop_cycle'])[2]['color'])
plt.xticks(x + width, labels=['a', 'b', 'c', 'd', 'e'])
plt.show()
```
