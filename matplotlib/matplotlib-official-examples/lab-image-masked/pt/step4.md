# Criando um Gráfico de Dispersão

Além de gráficos de linha, o Matplotlib também nos permite criar gráficos de dispersão (scatter plots). Gráficos de dispersão são úteis para visualizar a relação entre duas variáveis.

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
