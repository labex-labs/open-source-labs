# Crear un gráfico de barras

Matplotlib también puede crear gráficos de barras. Aquí hay un ejemplo:

```python
x = ['A', 'B', 'C', 'D', 'E']
y = [3, 7, 1, 9, 4]

plt.bar(x, y)
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Plot')
plt.show()
```
