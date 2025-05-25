# Criar um Gráfico de Dispersão (Scatter Plot)

Além dos gráficos de linha, o Matplotlib também pode criar gráficos de dispersão. Aqui está um exemplo:

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
