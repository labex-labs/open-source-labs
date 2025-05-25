# Criar um Gráfico de Linha Simples

Nesta etapa, criaremos um gráfico de linha simples usando Matplotlib. Começaremos gerando alguns dados para plotar usando a função `linspace()` do NumPy e a função `cos()`. Em seguida, usaremos a função `plot()` para criar o gráfico.

```python
t = np.linspace(0.0, 1.0, 100)
s = np.cos(4 * np.pi * t) + 2

plt.plot(t, s)
plt.show()
```
