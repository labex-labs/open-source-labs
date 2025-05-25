# Criar um Gráfico de Barras (Bar Chart)

Nesta etapa, criaremos um gráfico de barras usando Matplotlib. Começaremos gerando alguns dados para plotar usando a função `random()` do NumPy. Em seguida, usaremos a função `bar()` para criar o gráfico.

```python
x = ['A', 'B', 'C', 'D', 'E']
y = np.random.randint(1, 10, 5)

plt.bar(x, y)
plt.show()
```
