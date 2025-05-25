# Criar um Gráfico de Barras (Bar Plot)

O Matplotlib também pode criar gráficos de barras. Aqui está um exemplo:

```python
x = ['A', 'B', 'C', 'D', 'E']
y = [3, 7, 1, 9, 4]

plt.bar(x, y)
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Plot')
plt.show()
```
