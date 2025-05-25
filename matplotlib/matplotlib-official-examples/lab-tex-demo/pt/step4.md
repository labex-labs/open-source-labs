# Criar um Gráfico de Dispersão (Scatter Plot)

Nesta etapa, criaremos um gráfico de dispersão usando Matplotlib. Começaremos gerando alguns dados aleatórios para plotar usando a função `random()` do NumPy. Em seguida, usaremos a função `scatter()` para criar o gráfico.

```python
x = np.random.randn(100)
y = np.random.randn(100)

plt.scatter(x, y)
plt.show()
```
